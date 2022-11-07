from emora_stdm import DialogueFlow

chatbot = DialogueFlow('start')
transitions = {
    'state': 'start',
    '"Hello. How are you?"': {
        '[{fine, good, fantastic}]': {
            '"Glad to hear that you are doing well :)"': {
                'error': {
                    '"See you later!"': 'end'
                }
            }
        },
        'error': {
            '"I hope your day gets better soon :("': {
                'error': {
                    '"Take care!"': 'end'
                }
            }
        }
    }
}

if __name__ == '__main__':
    chatbot.load_transitions(transitions)
    chatbot.run()
