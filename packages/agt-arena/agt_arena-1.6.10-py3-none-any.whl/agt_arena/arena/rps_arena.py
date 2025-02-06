import os
import json
import docker
import requests
import logging
from datetime import datetime
import time
from tqdm import tqdm
from collections import defaultdict
from agt_arena.matchmaker.round_robin import RoundRobinMatchmaker

class RPSDockerArena():
    def __init__(self, num_rounds=10, submission_ids=[], setupTimeout: int = 5, totalMoveTimeout: int = 15, grace_time_per_move: float = 0.05, port = 5000):
        self.game_name = "Rock, Paper, Scissors"
        self.valid_actions = [0, 1, 2]
        self.utils = [[0, -1, 1], [1, 0, -1], [-1, 1, 0]]
        self.invalid_move_penalty = -1
        
        self.game_reports = defaultdict(lambda: {
            "action_history": [], 
            "util_history": [], 
        })
        
        self.num_rounds = num_rounds
        self.submission_ids = submission_ids
        self.setupTimeout = setupTimeout
        self.totalMoveTimeout = totalMoveTimeout
        self.grace_time_per_move = grace_time_per_move
        self.port = port
        

        self.client = docker.from_env()
        self.bot_names = {}
        self.bot_urls = {}
        self.health_checks(submission_ids)
    
        os.makedirs("logs", exist_ok=True)
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        log_filename = f"logs/rps/tournament_{timestamp}.log"
        logging.basicConfig(
            filename=log_filename,
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        self.totals_path = "meta/rps/totals.json"
        self.results_path = "meta/rps/results.json"
        
    
    def calculate_utils(self, p1_action, p2_action):
        if p1_action not in self.valid_actions and p2_action not in self.valid_actions:
            return [0, 0]
        if p1_action not in self.valid_actions:
            return [self.invalid_move_penalty, 0]
        if p2_action not in self.valid_actions:
            return [0, self.invalid_move_penalty]
        return [self.utils[p1_action][p2_action], self.utils[p2_action][p1_action]]

    def reset_game_reports(self):
        for player in self.players:
            self.game_reports[player.name]["action_history"] = []
            self.game_reports[player.name]["util_history"] = []

    def health_checks(self, submission_ids): 
        for bot_id in tqdm(submission_ids, desc = "Running Health Checks"): 
            _, url = RPSDockerArena.build_and_run_container(bot_id, self.port)
            print(f"URL sucessfully built: {url}")
            try: 
                name = self.health_check(url)
                if name and isinstance(name, str):
                    name = name.strip().replace("\t", "").replace("\n", "")
                    counter = 0
                    extension = ""
                    while any(name + extension == bot_name for bot_name in self.bot_names.values()): 
                        extension = f" ({counter + 1})"
                        counter += 1
                    name += extension
                        
                    print(f"{name} has sucessfully joined to the arena")
                    self.bot_names[bot_id] = name
                    self.bot_urls[bot_id] = url
                else:
                    print(f"Health check failed for bot-id: {bot_id}")
            finally: 
                RPSDockerArena.cleanup_container_and_image(bot_id)
        
    def health_check(self, url): 
        try:
            response = requests.get(f"{url}/health", timeout=15)
            if response.status_code == 200:
                status = response.json()
                if status.get("status") == "healthy" and "name" in status and isinstance(status["name"], str):
                    return status["name"]
            return None
        except requests.exceptions.RequestException as e:
            print(f"Health check failed for {url}: {e}")
            return None
    
    def build_and_run_container(bot_id, port, delay = 5):
        client = docker.from_env()
        image_name = f"rps_bot_{bot_id}"
        container_name = f"rps_container_{bot_id}"
        bot_port = port  # Port for this bot

        # Build the Docker image
        print(f"Building Docker image for bot {bot_id}...")
        try:
            build_logs = client.api.build(
                path=os.path.abspath("./"),
                dockerfile=os.path.abspath(f"./submissions/rps_submissions/{bot_id}/Dockerfile"),
                tag=image_name,
                rm=True,
                decode=True
            )
            for log in build_logs:
                if 'stream' in log:
                    print(log['stream'].strip())
                elif 'error' in log:
                    print(f"Build error: {log['error']}")
            print(f"Image for bot {bot_id} built successfully.")
        except docker.errors.BuildError as e:
            print(f"Error building image for bot {bot_id}: {e}")
            return None, None

        # Check if the image exists locally
        try:
            client.images.get(image_name)
        except docker.errors.ImageNotFound:
            print(f"Image {image_name} was not found after building. Exiting.")
            return None, None

        # Run the container
        print(f"Starting container for bot {bot_id}...")
        try:
            container = client.containers.run(
                image_name,
                name=container_name,
                detach=True,
                environment={
                    "BOT_PORT": bot_port,
                    "FLASK_ENV": "development",
                    "FLASK_DEBUG": "1",
                },
                healthcheck={
                    "test": ["CMD", "curl", "-f", f"http://{container_name}:{bot_port}/health"],
                    "interval": int(5e9),  # 5 seconds
                    "timeout": int(3e9),   # 3 seconds
                    "retries": 3,
                },
                volumes={
                    "/Users/johnwu/Documents/Brown CS/cs410_arena/logs/rps": {"bind": "/logs", "mode": "rw"},
                },
                network="tournament",
                tty=True,
                stdin_open=True
            )
            print(f"Container for bot {bot_id} is running.")
            time.sleep(delay)
            return container, f"http://{container_name}:{bot_port}"
        except docker.errors.APIError as e:
            print(f"Error starting container for bot {bot_id}: {e}")
            return None, f"http://{container_name}:{bot_port}"


    def cleanup_container_and_image(bot_id):
        client = docker.from_env()
        container_name = f"rps_container_{bot_id}"
        image_name = f"rps_bot_{bot_id}"

        #Stop and remove container
        print(f"Stopping and removing container for bot {bot_id}...")
        try:
            container = client.containers.get(container_name)
            container.stop()
            container.remove()
        except Exception as e:
            print(f"Error cleaning up container {container_name}: {e}")

        # # Remove image
        # print(f"Removing image for bot {bot_id}...")
        # try:
        #     client.images.remove(image_name, force=True)
        # except Exception as e:
        #     print(f"Error removing image {image_name}: {e}")
    
    def setup_bot(self, bot_url: str) -> bool:
        try:
            response = requests.post(
                f"{bot_url}/setup",
                timeout=self.setupTimeout
            )
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            logging.error(f"Error setting up bot at {bot_url}: {e}")
            return False
    
    def update_bot(self, bot_url: str, data) -> bool:
        try:
            response = requests.post(
                f"{bot_url}/update",
                json=data,
                timeout=self.setupTimeout
            )
            return response.status_code == 200
        except requests.exceptions.RequestException as e:
            logging.error(f"Error setting up bot at {bot_url}: {e}")
            return False
    
    def get_bot_move(self, bot_url):
        try:
            response = requests.post(f"{bot_url}/get_action", timeout=self.timeout)
            if response.status_code == 200:
                return response.json().get("action", -1)
        except requests.RequestException:
            logging.error(f"Bot at {bot_url} failed to respond.")
            return -1

    def run_match(self, p1_bot_id: int, p2_bot_id: int) -> dict:
        """Run a single match between two bots"""
        _, p1_bot_url = RPSDockerArena.build_and_run_container(p1_bot_id, self.port)
        _, p2_bot_url = RPSDockerArena.build_and_run_container(p2_bot_id, self.port)
        p1_name = self.bot_names[p1_bot_id]
        p2_name = self.bot_names[p2_bot_id]

        p1_total_util, p2_total_util = 0, 0
        
        try: 
            self.setup_bot(p1_bot_url)
            self.setup_bot(p2_bot_url)
            
            for _ in range(self.num_rounds):
                p1_action = self.get_bot_move(p1_bot_url)
                p2_action = self.get_bot_move(p2_bot_url)

                self.game_reports[p1_name]['action_history'].append(p1_action)
                self.game_reports[p2_name]['action_history'].append(p2_action)

                p1_util, p2_util = self.calculate_utils(p1_action, p2_action)
                self.game_reports[p1_name]["util_history"].append(p1_util)
                self.game_reports[p2_name]["util_history"].append(p2_util)
                
                p1_total_util += p1_util
                p2_total_util += p2_util
                
                self.update_bot(p1_bot_url, {
                    'my_action': p1_action, 
                    'opp_action': p2_action,
                    'my_util': p1_util,
                    'opp_util': p2_util
                })
                self.update_bot(p2_bot_url, {
                    'my_action': p2_action, 
                    'opp_action': p1_action,
                    'my_util': p2_util,
                    'opp_util': p1_util
                })
                
            game_summary = self._generate_game_summary(p1_name, p2_name)
            logging.info(game_summary)
            print(game_summary)
            
            return {
                'p1_total_util': p1_total_util,
                'p2_total_util': p2_total_util
            }
        
        finally:
            RPSDockerArena.cleanup_container_and_image(p1_bot_id)
            RPSDockerArena.cleanup_container_and_image(p2_bot_id)
        
    def _generate_game_summary(self, p1_name, p2_name):
        """
        Generate a summary for a specific game between two players.
        """
        p1_actions = self.game_reports[p1_name]["action_history"]
        p2_actions = self.game_reports[p2_name]["action_history"]
        p1_utils = self.game_reports[p1_name]["util_history"]
        p2_utils = self.game_reports[p2_name]["util_history"]

        p1_action_counts = {action: p1_actions.count(action) for action in self.valid_actions}
        p2_action_counts = {action: p2_actions.count(action) for action in self.valid_actions}
        p1_invalid_moves = len([a for a in p1_actions if a not in self.valid_actions])
        p2_invalid_moves = len([a for a in p2_actions if a not in self.valid_actions])
        p1_total_utility = sum(p1_utils)
        p2_total_utility = sum(p2_utils)

        return (
            f"Summary ({p1_name} VS {p2_name}):\n"
            f"{p1_name}: Played {p1_action_counts.get(0, 0)} Rocks, {p1_action_counts.get(1, 0)} Papers, "
            f"{p1_action_counts.get(2, 0)} Scissors; Invalid Moves: {p1_invalid_moves}; "
            f"Final Utility: {p1_total_utility}.\n"
            f"{p2_name}: Played {p2_action_counts.get(0, 0)} Rocks, {p2_action_counts.get(1, 0)} Papers, "
            f"{p2_action_counts.get(2, 0)} Scissors; Invalid Moves: {p2_invalid_moves}; "
            f"Final Utility: {p2_total_utility}.\n"
        )
    
    def run_tournament(self):
        results = []
        bot_ids = list(self.bot_names.keys())
        
        try:
            with open(self.totals_path, "r") as f:
                existing_stats = json.load(f)
        except FileNotFoundError:
            existing_stats = {}

        bot_stats = {
            bot_id: existing_stats.get(
                bot_id, 
                {'total_utility': 0.0, 'rounds': 0}
            )
            for bot_id in bot_ids
        }
    
        matchmaker = RoundRobinMatchmaker(order_matters=False)
        matchups = matchmaker.generate_matches(bot_ids)
        num_matchups = len(matchups)

        for p1_bot_id, p2_bot_id in tqdm(matchups, desc="Running matches", total=num_matchups):
            p1_name = self.bot_names[p1_bot_id]
            p2_name = self.bot_names[p2_bot_id]
            print(f"\nStarting match: {p1_name} vs {p2_name}")
            results = self.run_match(p1_bot_id, p2_bot_id)
            
            bot_stats[p1_bot_id]['rounds'] += self.num_rounds
            bot_stats[p2_bot_id]['rounds'] += self.num_rounds
            
            bot_stats[p1_bot_id]['total_utility'] += results['p1_total_util']
            bot_stats[p2_bot_id]['total_utility'] += results['p2_total_util']
            
            with open(self.totals_path, "w") as f:
                json.dump(bot_stats, f, indent=4)
        
        results_data = {}
        for bot, stats in tqdm(bot_stats.items(), desc="Calculating Stats"):
            avg_score = stats['total_utility'] / stats['rounds'] if stats['rounds'] > 0 else 0.0
            logging.info(f"Bot {stats['name']}: Total Score: {stats['total_utility']}, Rounds: {stats['rounds']},  Average Score: {avg_score}")
            results_data[bot] = {
                "name": stats['name'],
                "total_utility": stats['total_utility'],
                "average_utility": (stats["total_utility"]) / stats["rounds"] if stats["rounds"] > 0 else 0.0,
            }
            
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        results_path_timestamp = f"{self.results_path.rstrip('.json')}_{timestamp}.json"
        with open(results_path_timestamp, "w") as f:
            json.dump(results_data, f, indent=4)

        return results
