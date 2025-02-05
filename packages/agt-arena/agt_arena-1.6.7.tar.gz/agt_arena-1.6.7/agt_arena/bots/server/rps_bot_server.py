from flask import Flask, request, jsonify


def create_bot_server(bot_factory):
    """Factory function to create a Flask server for any bot"""
    app = Flask(__name__)
    bot = bot_factory()

    @app.route('/get_move', methods=['POST'])
    def get_move():
        move = bot.get_action()
        return jsonify({'move': move})

    @app.route('/setup', methods=['POST'])
    def setup():
        bot.restart()
        return jsonify({'status': 'ready'})
    
    @app.route('/update', methods=['POST'])
    def update():
        my_action = request.json['my_action']
        opp_action = request.json['opp_action']
        my_util = request.json['my_util']
        opp_util = request.json['opp_util']
        
        bot.update()
        bot.game_report.game_history['my_action_history'].append(my_action)
        bot.game_report.game_history['opp_action_history'].append(opp_action)
        bot.game_report.game_history['my_utils_history'].append(my_util)
        bot.game_report.game_history['opp_utils_history'].append(opp_util)
        
        return jsonify({'status': 'updated'})

    @app.route('/health', methods=['GET'])
    def health_check():
        print(str(bot))
        if str(bot) is None:
            return jsonify({'status': 'unhealthy'}), 100
        else:
            return jsonify({'status': 'healthy', 'name': str(bot)}), 200

    return app


def run_bot_server(bot_factory, port):
    """Convenience function to create and run a bot server"""
    print(f"Running bot server for {bot_factory.__name__}")
    app = create_bot_server(bot_factory)
    app.run(host='0.0.0.0', port=port, debug=True)