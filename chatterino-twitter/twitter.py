from TwitterAPI import TwitterAPI
import json

api = TwitterAPI('MVQFasenNHIhrCFXqjgVmpLez', 
                'prMQqxjQcAv2VKIgZlpqKBFu8yYVzIv9IlTSzm6XPzDg0gePFp',
                '1255862538442547201-J5o1oXwfahCMKRINeVLmQGE6rFHEMn',
                'FOysob16EQmFIsKlRippSddfSgi2sWIOp71QtKF8HEJDY'
                )

def send_message(user_id, message):
    event = {
	    "event": {
	    	"type": "message_create",
	    	"message_create": {
	    		"target": {
	    			"recipient_id": user_id
	    		},
	    		"message_data": {
	    			"text": message
		    	}
    		}
    	}
    }
    r = api.request('direct_messages/events/new', json.dumps(event))
    print('SUCCESS' if r.status_code == 200 else 'PROBLEM: ' + r.text)