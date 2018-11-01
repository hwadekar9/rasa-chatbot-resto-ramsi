## Generated Story 255706069223404498
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": ["more","300"]}
    - slot{"price":"300"}
    - action_restaurant
	- slot{"noresults": false}
	- utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email":"sanesanyo@gmail.com"}
	- action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 25570606922340039495
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
	- action_city
    - slot{"location_type": false}
    - utter_nontier
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 1993277579540566202
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "North Indian"}
    - slot{"cuisine": "North Indian"}
	- utter_ask_price
* restaurant_search{"price": ["greater","700"]}
    - slot{"price":"low"}
    - action_restaurant
	- slot{"noresults": false}
	- utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email":"sanyog.yadav@gmx.net"}
	- action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 3320800183399695936
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "italy"}
    - slot{"location": "italy"}
	- action_city
    - slot{"location_type": false}
    - utter_nontier
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -4639179087166749998
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
	- utter_ask_price
* restaurant_search{"price": ["max","300"]}
    - slot{"price":["max","300"]}
    - action_restaurant
	- slot{"noresults": true}
	- utter_noresults
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 4963448062290237512
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
	- action_city
	- slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
	- utter_ask_price
* restaurant_search{"price": ["less","300"]}
    - slot{"price":["less","300"]}
    - action_restaurant
	- slot{"noresults": true}
	- utter_noresults
* deny
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 3395544653359458884
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": ["more","700"]}
    - slot{"price":["more","700"]}
    - action_restaurant
	- slot{"noresults": true}
	- utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
	- action_restarted
	
## Generated Story 2424409812633241572
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": ["more","700"]}
    - slot{"price":["more","700"]}
    - action_restaurant
	- slot{"noresults": false}
	- utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email":"santhosh.prakash@gmail.com"}
	- action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted


## Generated Story -958185873477169632
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bhopal"}
    - slot{"location": "bhopal"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": ["greater","700"]}
    - slot{"price":["greater","700"]}
    - action_restaurant
	- slot{"noresults": false}
    - action_restaurant
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email":"sanyog.yadav@gmx.net"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -3450322879838263636
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["700"]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -6618205134182014576
* greet
    - utter_greet
* restaurant_search{"location": "saharanpur"}
    - slot{"location": "saharanpur"}
    - action_city
    - slot{"location_type": false}
    - utter_nontier
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["700"]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* goodbye{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -3903772308407583072
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["700"]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -4516450081715921164
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["700"]}
    - action_restaurant
    - slot{"noresults": true}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* restaurant_search{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -3122543126751166243
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": [0, "300"]}
    - action_restaurant
    - slot{"noresults": true}
    - utter_noresults
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -1555280997735521460
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price": "800"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": ["300", "800"]}
    - action_city
    - slot{"location_type": true}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - action_reset
	- action_restarted

## Generated Story 1810161726509399194
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["300", "700"]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -4062443355466053087
* greet
    - utter_greet
* restaurant_search{"cuisine": "north indian", "location": "delhi"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": ["300", 0]}
    - action_restaurant
    - slot{"noresults": true}
    - utter_noresults
* restaurant_search{"price": "800"}
    - slot{"price": ["300", "800"]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 3443504586412887994
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "pune"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": [0, "300"]}
    - action_restaurant
    - slot{"noresults": true}
    - utter_noresults
* restaurant_search{"cuisine": "american", "location": "price", "price": "800"}
    - slot{"cuisine": "american"}
    - slot{"location": "price"}
    - slot{"price": ["300", "800"]}
    - action_restaurant
    - slot{"noresults": true}
    - utter_noresults
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 3192468543823603100
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_city
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["700"]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_ifmail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -876334346752649206
* greet
    - utter_greet
* restaurant_search{"location": "bengaluru"}
    - slot{"location": "bengaluru"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* send_mail{"cuisine": "chainese"}
    - slot{"cuisine": "chainese"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["700"]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* goodbye
    - utter_goodbye
	- action_reset
	- action_restarted

## Generated Story -2347810003025567463
* restaurant_search{"location": "dilli"}
    - slot{"location": "dilli"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* send_mail{"cuisine": "maxican"}
    - slot{"cuisine": "maxican"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["300", "700"]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 4858673086685401740
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "south - indian"}
    - slot{"cuisine": "south - indian"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": [0, "300"]}
    - action_restaurant
    - slot{"cuisine": "south indian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -4247965377061863541
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": [0, "300"]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset

## Generated Story 3234413932400209490
* greet
    - utter_greet
* restaurant_search{"cuisine": "chianese", "location": "chennai"}
    - slot{"cuisine": "chianese"}
    - slot{"location": "chennai"}
    - action_city
    - slot{"location": "chennai"}
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "50"}
    - slot{"price": [0, "50"]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": true}
    - utter_noresults
* restaurant_search{"cuisine": "american", "price": "400"}
    - slot{"cuisine": "american"}
    - slot{"price": ["300", "400"]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 553583631579008536
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": ["500", "800"]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - action_reset
	- action_restarted

## Generated Story 1153400723468589605
* greet
    - utter_greet
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_city
    - slot{"location": "jaipur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* send_mail{"cuisine": "chianese"}
    - slot{"cuisine": "chianese"}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": ["400", "800"]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* thankyou
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -5145876738353750775
* restaurant_search{"location": "patna"}
    - slot{"location": "patna"}
    - action_city
    - slot{"location": "patna"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "670"}
    - slot{"price": ["350", "670"]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - action_reset
	- action_restarted

## Generated Story -5707329669200666817
* restaurant_search{"location": "kolkata"}
    - slot{"location": "kolkata"}
    - action_city
    - slot{"location": "kolkata"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "mexican"}
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": ["450", "800"]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* thankyou
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -5450921290298582452
* greet
    - utter_greet
* restaurant_search{"location": "ladakh"}
    - slot{"location": "ladakh"}
    - action_city
    - slot{"location": "ladakh"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "srinagar"}
    - slot{"location": "srinagar"}
    - action_city
    - slot{"location": "srinagar"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "900"}
    - slot{"price": ["500", "900"]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sara.topmann@gmx.de"}
    - slot{"email": "sara.topmann@gmx.de"}
    - action_send_mail
    - action_reset
	- action_restarted

## Generated Story 6950907805263641888
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "trivandrum"}
    - slot{"location": "trivandrum"}
    - action_city
    - slot{"location": "thiruvananthapuram"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* send_mail{"cuisine": "chianese"}
    - slot{"cuisine": "chianese"}
    - utter_ask_price
* restaurant_search{"price": "900"}
    - slot{"price": ["400", "900"]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* send_mail{"email": "random.dude@yahoo.co.uk"}
    - slot{"email": "random.dude@yahoo.co.uk"}
    - action_send_mail
* thankyou
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -6044468681819301497
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["400", "700"]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - action_reset
	- action_restarted

## Generated Story -1469174573020217835
* restaurant_search{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_city
    - slot{"location": "berlin"}
    - slot{"location_type": false}
    - utter_nontier
* affirm
    - utter_noresults
* deny
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 2036387574549953528
* greet
    - utter_greet
* restaurant_search{"location": "frankfurt"}
    - slot{"location": "frankfurt"}
    - action_city
    - slot{"location": "frankfurt"}
    - slot{"location_type": false}
    - utter_nontier
* affirm
    - utter_noresults
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_city
    - slot{"location": "jaipur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "789"}
    - slot{"price": ["500", "789"]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* thankyou
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 5803076505926652526
* greet
    - utter_greet
* restaurant_search{"location": "delh"}
    - slot{"location": "delh"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "400"}
    - slot{"price": ["400"]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -8738653747588024438
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "1"}
    - action_get_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* restaurant_search{"price": "700"}
    - slot{"price": ["700"]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
* thankyou
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -1491451145424978920
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* getnum{"num": "2"}
	- action_get_price
    - slot{"price": [300,700]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - slot{"email": null}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
	- action_restarted


## Generated Story -1491451145424978921
* greet
    - utter_greet
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "4"}
	- action_get_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* getnum{"num": "2"}
    - action_get_price
    - slot{"price": [300,700]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - slot{"email": null}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story 8659567337808660971
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "5"}
    - action_get_cuisine
    - slot{"cuisine": "south indian"}
    - utter_ask_price
* getnum{"num": "3"}
    - action_get_price
    - slot{"price": [700]}
    - action_restaurant
    - slot{"cuisine": "south indian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
    - action_reset
	- action_restarted

## Generated Story 8659567337808660973
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian", "location": "delhi"}
    - slot{"cuisine": "italian"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "3"}
    - action_get_price
    - slot{"price": [700]}
    - action_restaurant
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - action_reset
	- action_restarted
	
## Generated Story -4468821474829087708
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "4"}
    - slot{"num": "4"}
    - action_get_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - slot{"email": null}
    - utter_ask_ifmail
* affirm{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* thankyou
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -6480769639985676319
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "1"}
    - slot{"num": "1"}
    - action_get_price
    - slot{"price": [0, 300]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -3027922206456805934
* greet
    - utter_greet
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_price
    - slot{"price": [700, 0]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* thankyou
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
* goodbye
    - utter_goodbye
    - action_reset
	- action_restarted

## Generated Story -2349910242551578877
* greet
    - utter_greet
* restaurant_search{"location": "paris"}
    - slot{"location": "paris"}
    - action_city
    - slot{"location": "paris"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "london"}
    - slot{"location": "london"}
    - action_city
    - slot{"location": "london"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 7293693463062710526
* restaurant_search{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_city
    - slot{"location": "berlin"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "bombay"}
    - slot{"location": "bombay"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -1714002399065678550
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_price
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_price
    - slot{"price": [700, 0]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -2387068036647081793
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_price
    - slot{"price": [700, 0]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -5110707230971152273
* user_ask
    - utter_userask
* restaurant_search{"cuisine": "chinese", "location": "delhi"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "900"}
    - slot{"price": ["400", "900"]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 6510232678487480145
* about_yourself
    - utter_aboutyourself
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "bombay"}
    - slot{"location": "bombay"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_price
    - slot{"price": [700, 0]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
* thankyou
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 4087234082453484783
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search{"cuisine": "chinese"}
    - slot{"cuisine": "chinese"}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -8148068614550623057
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_city
    - slot{"location": "chennai"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -5159164613671623109
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_city
    - slot{"location": "chennai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 4317822914391937023
* user_ask
    - utter_userask
* restaurant_search{"cuisine": "chinese", "location": "mumbai"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_price
    - slot{"price": [700, 0]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 106224107127410464
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* user_ask
    - utter_userask
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -8375065483608308746
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* user_ask
    - utter_userask
* restaurant_search{"cuisine": "american", "location": "mumbai"}
    - slot{"cuisine": "american"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 1441502188118997316
* greet
    - utter_greet
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "300"}
    - slot{"price": ["300"]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -4584439607893482527
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* user_ask
    - utter_userask
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "500"}
    - slot{"price": [0, "500"]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -4681062017331307515
* user_ask
    - utter_userask
* restaurant_search{"location": "bombay"}
    - slot{"location": "bombay"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "4"}
    - slot{"num": "4"}
    - action_get_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": ["400", "800"]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - export

## Generated Story -1374493019790478621
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search{"location": "calcutta"}
    - slot{"location": "calcutta"}
    - action_city
    - slot{"location": "kozhikode"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_price
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_price
    - slot{"price": [700, 0]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": true}
    - utter_noresults
* restaurant_search{"location": "bombay"}
    - slot{"location": "bombay"}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -3043581327404935308
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* user_ask
    - utter_userask
* restaurant_search{"cuisine": "south indian", "location": "delli"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "delli"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_price
    - slot{"price": [700, 0]}
    - action_restaurant
    - slot{"cuisine": "south indian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 1437890508483397116
* greet
    - utter_greet
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_location
* restaurant_search
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 5502548590108688761
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": ["800"]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* affirm
    - utter_ask_mail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -4791265416238318095
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "1"}
    - slot{"num": "1"}
    - action_get_price
    - slot{"price": [0, 300]}
    - action_restaurant
    - slot{"cuisine": "north indian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -1322003216220927989
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "bangalore"}
    - slot{"location": "bangalore"}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -2146093293056152142
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_city
    - slot{"location": "jaipur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "40"}
    - slot{"price": ["0", "40"]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": true}
    - utter_noresults
* restaurant_search{"price": "500"}
    - slot{"price": ["400", "500"]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 1881084630317718915
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_city
    - slot{"location": "chennai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* restaurant_search{"cuisine": "american"}
    - slot{"cuisine": "american"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 5786222051380181771
* greet
    - utter_greet
* restaurant_search{"cuisine": "italian"}
    - slot{"cuisine": "italian"}
    - utter_ask_location
* restaurant_search{"location": "bombay"}
    - slot{"location": "bombay"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -2155460509267956945
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* restaurant_search{"location": "paris"}
    - slot{"location": "paris"}
    - action_city
    - slot{"location": "paris"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "berlin"}
    - slot{"location": "berlin"}
    - action_city
    - slot{"location": "berlin"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 1461717959664878483
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search{"location": "london"}
    - slot{"location": "london"}
    - action_city
    - slot{"location": "london"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "madrid"}
    - slot{"location": "madrid"}
    - action_city
    - slot{"location": "madrid"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -9152706463634804587
* greet
    - utter_greet
* restaurant_search{"location": "raipur"}
    - slot{"location": "raipur"}
    - action_city
    - slot{"location": "raipur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "1"}
    - slot{"num": "1"}
    - action_get_cuisine
    - slot{"cuisine": "chinese"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 4494157121401289416
* about_yourself
    - utter_aboutyourself
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "rampur"}
    - slot{"location": "rampur"}
    - action_city
    - slot{"location": "rampur"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "vishakapatnam"}
    - slot{"location": "vishakapatnam"}
    - action_city
    - slot{"location": "visakhapatnam"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -895717287815279996
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* restaurant_search{"location": "kohlapur"}
    - slot{"location": "kohlapur"}
    - action_city
    - slot{"location": "kolhapur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 6812914199624472895
* about_yourself
    - utter_aboutyourself
* restaurant_search{"location": "kolhapur"}
    - slot{"location": "kolhapur"}
    - action_city
    - slot{"location": "kolhapur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -1131761436619973171
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search
    - utter_ask_location
* restaurant_search
    - action_city
    - slot{"location": "unknown"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 3469288313526680297
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search{"location": "bombay"}
    - slot{"location": "bombay"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_cuisine
    - slot{"cuisine": "italian"}
    - utter_ask_price
* restaurant_search{"price": "900"}
    - slot{"price": [0, "900"]}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -7780293713927600454
* restaurant_search
    - utter_ask_location
* restaurant_search{"location": "bombay"}
    - slot{"location": "bombay"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* restaurant_search{"price": "800"}
    - slot{"price": ["300", "800"]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -7743156677249845795
* restaurant_search{"cuisine": "italian", "location": "bangalore", "price": "1000"}
    - slot{"cuisine": "italian"}
    - slot{"location": "bangalore"}
    - slot{"price": ["500", "1000"]}
    - action_city
    - slot{"location": "bengaluru"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
* thankyou
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -7559446012123882992
* restaurant_search{"cuisine": "chinese", "location": "mumbai", "price": "900"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - slot{"price": ["300", "900"]}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 2739676398323380040
* restaurant_search{"cuisine": "italian", "location": "saharanpur", "price": "800"}
    - slot{"cuisine": "italian"}
    - slot{"location": "saharanpur"}
    - slot{"price": ["300", "800"]}
    - action_city
    - slot{"location": "saharanpur"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -3869334245952596015
* restaurant_search{"cuisine": "north indian", "location": "mumbai", "price": "900"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "mumbai"}
    - slot{"price": ["300", "900"]}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "north indian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -706098079771257315
* restaurant_search{"cuisine": "chinese", "location": "varansi", "price": "800"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "varansi"}
    - slot{"price": ["300", "800"]}
    - action_city
    - slot{"location": "varanasi"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -4146321868584786862
* restaurant_search{"cuisine": "chianese", "location": "bhillai", "price": "900"}
    - slot{"cuisine": "chianese"}
    - slot{"location": "bhillai"}
    - slot{"price": ["400", "900"]}
    - action_city
    - slot{"location": "bhillai"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "faridabad"}
    - slot{"location": "faridabad"}
    - action_city
    - slot{"location": "faridabad"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 3420730573897693455
* restaurant_search{"cuisine": "mexican", "location": "surat", "price": "670"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "surat"}
    - slot{"price": ["350", "670"]}
    - action_city
    - slot{"location": "surat"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "ahmedabad"}
    - slot{"location": "ahmedabad"}
    - action_city
    - slot{"location": "ahmedabad"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
* thankyou
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -4853906693024315442
* restaurant_search{"cuisine": "south indian", "location": "rajkot"}
    - slot{"cuisine": "south indian"}
    - slot{"location": "rajkot"}
    - action_city
    - slot{"location": "rajkot"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "south indian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 7410470582737395875
* restaurant_search{"cuisine": "mexican", "location": "jamnagar", "price": "900"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "jamnagar"}
    - slot{"price": ["300", "900"]}
    - action_city
    - slot{"location": "jamnagar"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - export

## Generated Story -5295308009656838346
* restaurant_search{"price": "900"}
    - slot{"price": ["300", "900"]}
    - utter_ask_location
* restaurant_search{"location": "guntur"}
    - slot{"location": "guntur"}
    - action_city
    - slot{"location": "guntur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_cuisine
    - slot{"cuisine": "mexican"}
    - utter_ask_price
* getnum{"num": "1"}
    - slot{"num": "1"}
    - action_get_price
    - slot{"price": [0, 300]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": true}
    - utter_noresults
* restaurant_search{"price": "1500"}
    - slot{"price": ["600", "1500"]}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -6368286923827132188
* restaurant_search{"location": "kohlapur", "price": "900"}
    - slot{"location": "kohlapur"}
    - slot{"price": ["300", "900"]}
    - action_city
    - slot{"location": "kolhapur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -5066545551573104497
* restaurant_search{"cuisine": "chinese", "location": "dehradun", "price": "850"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "dehradun"}
    - slot{"price": ["500", "850"]}
    - action_city
    - slot{"location": "dehradun"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -6357008507192732117
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price": "600"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": ["300", "600"]}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -7286029270907498585
* restaurant_search{"cuisine": "chianese", "location": "mumbai", "price": "500"}
    - slot{"cuisine": "chianese"}
    - slot{"location": "mumbai"}
    - slot{"price": ["300", "500"]}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 3896095818508343480
* restaurant_search{"location": "mumbai", "price": "800"}
    - slot{"location": "mumbai"}
    - slot{"price": ["300", "800"]}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "3"}
    - slot{"num": "3"}
    - action_get_cuisine
    - slot{"cuisine": "italian"}
    - action_restaurant
    - slot{"cuisine": "italian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 7283089863615493336
* restaurant_search{"cuisine": "chinese", "location": "mumbai", "price": "800"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - slot{"price": ["500", "800"]}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -6435407930804281282
* restaurant_search{"cuisine": "north indian", "location": "pune", "price": "890"}
    - slot{"cuisine": "north indian"}
    - slot{"location": "pune"}
    - slot{"price": ["500", "890"]}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "north indian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -4113051316603878164
* restaurant_search{"cuisine": "mexican", "location": "rewari", "price": "1200"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "rewari"}
    - slot{"price": ["500", "1200"]}
    - action_city
    - slot{"location": "rewari"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_city
    - slot{"location": "jaipur"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -5863114944456660062
* restaurant_search{"location": "katuwas", "price": "900"}
    - slot{"location": "katuwas"}
    - slot{"price": ["500", "900"]}
    - action_city
    - slot{"location": "katuwas"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "jaipur"}
    - slot{"location": "jaipur"}
    - action_city
    - slot{"location": "jaipur"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "4"}
    - slot{"num": "4"}
    - action_get_cuisine
    - slot{"cuisine": "american"}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* send_mail{"email": "sanesanyo@gmail.com"}
    - slot{"email": "sanesanyo@gmail.com"}
    - action_send_mail
    - slot{"email": "sanesanyo@gmail.com"}
* goodbye
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -8303399343053257340
* restaurant_search{"cuisine": "chinese", "price": "1200"}
    - slot{"cuisine": "chinese"}
    - slot{"price": ["500", "1200"]}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 3268517013016360024
* restaurant_search{"cuisine": "north indian"}
    - slot{"cuisine": "north indian"}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_price
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_price
    - slot{"price": [300, 700]}
    - action_restaurant
    - slot{"cuisine": "north indian"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 4444591927782236181
* restaurant_search{"cuisine": "chinese", "price": "450"}
    - slot{"cuisine": "chinese"}
    - slot{"price": ["450", 0]}
    - utter_ask_location
* restaurant_search{"location": "pune"}
    - slot{"location": "pune"}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 6780835164616500110
* restaurant_search{"price": "900"}
    - slot{"price": ["500", "900"]}
    - utter_ask_location
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "4"}
    - slot{"num": "4"}
    - action_get_cuisine
    - slot{"cuisine": "american"}
    - action_restaurant
    - slot{"cuisine": "american"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -5686742880495568154
* restaurant_search{"cuisine": "chinese", "location": "sanoli", "price": "100"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "sanoli"}
    - slot{"price": ["500", "100"]}
    - action_city
    - slot{"location": "shimla"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 4660648306605827843
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* restaurant_search{"cuisine": "chinese", "price": "500"}
    - slot{"cuisine": "chinese"}
    - slot{"price": ["300", "500"]}
    - utter_ask_location
* restaurant_search{"location": "mumbai"}
    - slot{"location": "mumbai"}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 6519626969874549223
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "mumbai", "price": "1000"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "mumbai"}
    - slot{"price": ["500", "1000"]}
    - action_city
    - slot{"location": "mumbai"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 7143519918602168485
* greet
    - utter_greet
* restaurant_search{"cuisine": "chinese", "location": "chennai", "price": "1000"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "chennai"}
    - slot{"price": ["500", "1000"]}
    - action_city
    - slot{"location": "chennai"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 8346763385617086459
* greet
    - utter_greet
* restaurant_search{"cuisine": "mexican", "location": "calcutta", "price": "1500"}
    - slot{"cuisine": "mexican"}
    - slot{"location": "calcutta"}
    - slot{"price": ["500", "1500"]}
    - action_city
    - slot{"location": "kolkata"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": true}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story -3712443714285110760
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search{"cuisine": "chinese", "location": "kolkata", "price": "1000"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "kolkata"}
    - slot{"price": ["500", "1000"]}
    - action_city
    - slot{"location": "kolkata"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 7888134918482423316
* greet
    - utter_greet
* about_yourself
    - utter_aboutyourself
* user_ask
    - utter_userask
* restaurant_search{"cuisine": "chinese", "location": "pune", "price": "900"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "pune"}
    - slot{"price": ["300", "900"]}
    - action_city
    - slot{"location": "pune"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 1256552808505157980
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search{"cuisine": "chinese", "location": "saharanpur", "price": "1000"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "saharanpur"}
    - slot{"price": ["500", "1000"]}
    - action_city
    - slot{"location": "saharanpur"}
    - slot{"location_type": false}
    - utter_nontier
    - utter_noresults
* restaurant_search{"location": "delhi"}
    - slot{"location": "delhi"}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 5337503150368073728
* restaurant_search{"cuisine": "chinese", "location": "delhi", "price": "1000"}
    - slot{"cuisine": "chinese"}
    - slot{"location": "delhi"}
    - slot{"price": ["500", "1000"]}
    - action_city
    - slot{"location": "delhi"}
    - slot{"location_type": true}
    - action_restaurant
    - slot{"cuisine": "chinese"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

## Generated Story 1391576416241737108
* greet
    - utter_greet
* user_ask
    - utter_userask
* restaurant_search{"price": "1000"}
    - slot{"price": ["500", "1000"]}
    - utter_ask_location
* restaurant_search{"location": "chennai"}
    - slot{"location": "chennai"}
    - action_city
    - slot{"location": "chennai"}
    - slot{"location_type": true}
    - utter_ask_cuisine
* getnum{"num": "2"}
    - slot{"num": "2"}
    - action_get_cuisine
    - slot{"cuisine": "mexican"}
    - action_restaurant
    - slot{"cuisine": "mexican"}
    - slot{"noresults": false}
    - utter_ask_ifmail
* deny
    - utter_goodbye
    - action_reset
    - reset_slots
    - action_restarted

