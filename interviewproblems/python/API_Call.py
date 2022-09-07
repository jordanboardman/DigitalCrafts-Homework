# NOT COMPLETE
# 
# Using python, make an API call to the random user api. Retrieve 10 users and store the first and last name of each user you retrieve. Store the list of users in alphabetical order by last name.

# pip install for import requests

import requests
import json

# response_API = requests.get('https://random-data-api.com/api/v2/users?size=10&is_xml=true')

# data = response_API.text

# json.loads(data)

# ??

# Originally, I pulled the API through Postman and copy+paste the call below, but that's not the best practice. Need to loop through the call and get this less lines of code.
# users = [
#     {
#         "id": 9739,
#         "uid": "959ab55d-42a0-4cbc-88bc-e9fc39313190",
#         "password": "V0gD5MusHK",
#         "first_name": "Mitch",
#         "last_name": "Zieme",
#         "username": "mitch.zieme",
#         "email": "mitch.zieme@email.com",
#         "avatar": "https://robohash.org/estidfacilis.png?size=300x300&set=set1",
#         "gender": "Genderqueer",
#         "phone_number": "+64 432-344-8601 x66625",
#         "social_insurance_number": "377511720",
#         "date_of_birth": "1963-01-19",
#         "employment": {
#             "title": "Chief IT Consultant",
#             "key_skill": "Organisation"
#         },
#         "address": {
#             "city": "New Chetshire",
#             "street_name": "Crist Park",
#             "street_address": "2376 Considine Points",
#             "zip_code": "57599-4055",
#             "state": "New Jersey",
#             "country": "United States",
#             "coordinates": {
#                 "lat": 47.573782357083246,
#                 "lng": 67.4090572654903
#             }
#         },
#         "credit_card": {
#             "cc_number": "4561808199316"
#         },
#         "subscription": {
#             "plan": "Silver",
#             "status": "Blocked",
#             "payment_method": "Credit card",
#             "term": "Payment in advance"
#         }
#     },
#     {
#         "id": 6050,
#         "uid": "a1eda4aa-fbf8-40a5-95b9-d75c116e8d52",
#         "password": "MwyA0nPtrH",
#         "first_name": "Drusilla",
#         "last_name": "Osinski",
#         "username": "drusilla.osinski",
#         "email": "drusilla.osinski@email.com",
#         "avatar": "https://robohash.org/accusantiuminciduntnihil.png?size=300x300&set=set1",
#         "gender": "Polygender",
#         "phone_number": "+52 (443) 722-0295",
#         "social_insurance_number": "599943644",
#         "date_of_birth": "1993-10-31",
#         "employment": {
#             "title": "Customer Design Consultant",
#             "key_skill": "Problem solving"
#         },
#         "address": {
#             "city": "East Waynemouth",
#             "street_name": "Gorczany Place",
#             "street_address": "785 Waters Street",
#             "zip_code": "59052",
#             "state": "Hawaii",
#             "country": "United States",
#             "coordinates": {
#                 "lat": -34.54183196037402,
#                 "lng": -106.26782117773911
#             }
#         },
#         "credit_card": {
#             "cc_number": "4501830550805"
#         },
#         "subscription": {
#             "plan": "Student",
#             "status": "Active",
#             "payment_method": "Money transfer",
#             "term": "Annual"
#         }
#     },
#     {
#         "id": 4176,
#         "uid": "0482fbbf-7bb7-4c5d-ad73-f29dfab216e8",
#         "password": "dUiAPVlDFL",
#         "first_name": "Sid",
#         "last_name": "Mosciski",
#         "username": "sid.mosciski",
#         "email": "sid.mosciski@email.com",
#         "avatar": "https://robohash.org/adipiscietet.png?size=300x300&set=set1",
#         "gender": "Bigender",
#         "phone_number": "+975 804-150-2406 x316",
#         "social_insurance_number": "732928502",
#         "date_of_birth": "1988-10-23",
#         "employment": {
#             "title": "Sales Liaison",
#             "key_skill": "Fast learner"
#         },
#         "address": {
#             "city": "Aufderharstad",
#             "street_name": "Murphy Club",
#             "street_address": "836 Green Heights",
#             "zip_code": "56246",
#             "state": "Rhode Island",
#             "country": "United States",
#             "coordinates": {
#                 "lat": 38.86258094905935,
#                 "lng": 28.133992853751977
#             }
#         },
#         "credit_card": {
#             "cc_number": "4682-7655-7254-6328"
#         },
#         "subscription": {
#             "plan": "Student",
#             "status": "Idle",
#             "payment_method": "Alipay",
#             "term": "Monthly"
#         }
#     },
#     {
#         "id": 807,
#         "uid": "041afd40-b3bc-4287-97b3-c5804ce7f24d",
#         "password": "WbgK2vhpyz",
#         "first_name": "Nathan",
#         "last_name": "Littel",
#         "username": "nathan.littel",
#         "email": "nathan.littel@email.com",
#         "avatar": "https://robohash.org/natustemporeut.png?size=300x300&set=set1",
#         "gender": "Female",
#         "phone_number": "+1-345 246-390-7775 x656",
#         "social_insurance_number": "565133733",
#         "date_of_birth": "1963-03-29",
#         "employment": {
#             "title": "Technology Facilitator",
#             "key_skill": "Teamwork"
#         },
#         "address": {
#             "city": "New Morganberg",
#             "street_name": "Taunya Expressway",
#             "street_address": "81927 Antoine Garden",
#             "zip_code": "49171-6087",
#             "state": "Ohio",
#             "country": "United States",
#             "coordinates": {
#                 "lat": -81.89518331151896,
#                 "lng": -89.12873868017508
#             }
#         },
#         "credit_card": {
#             "cc_number": "5354-8115-5916-1493"
#         },
#         "subscription": {
#             "plan": "Professional",
#             "status": "Idle",
#             "payment_method": "Debit card",
#             "term": "Annual"
#         }
#     },
#     {
#         "id": 5994,
#         "uid": "f957d824-8c9c-4f78-950c-d805e5fe4c93",
#         "password": "5hoJLQSDxk",
#         "first_name": "Rachal",
#         "last_name": "Price",
#         "username": "rachal.price",
#         "email": "rachal.price@email.com",
#         "avatar": "https://robohash.org/dolorquamaperiam.png?size=300x300&set=set1",
#         "gender": "Non-binary",
#         "phone_number": "+503 1-659-159-1964",
#         "social_insurance_number": "688388628",
#         "date_of_birth": "1962-08-21",
#         "employment": {
#             "title": "Advertising Strategist",
#             "key_skill": "Confidence"
#         },
#         "address": {
#             "city": "Olivemouth",
#             "street_name": "Yael Squares",
#             "street_address": "28408 Thompson Ways",
#             "zip_code": "41098",
#             "state": "New Mexico",
#             "country": "United States",
#             "coordinates": {
#                 "lat": 29.047594919059065,
#                 "lng": -9.820693473738345
#             }
#         },
#         "credit_card": {
#             "cc_number": "4266738371171"
#         },
#         "subscription": {
#             "plan": "Basic",
#             "status": "Active",
#             "payment_method": "Alipay",
#             "term": "Full subscription"
#         }
#     },
#     {
#         "id": 6883,
#         "uid": "340e3022-0e7a-4f91-b658-e806dae0c52e",
#         "password": "uWMfKkn5p2",
#         "first_name": "Russell",
#         "last_name": "Jacobi",
#         "username": "russell.jacobi",
#         "email": "russell.jacobi@email.com",
#         "avatar": "https://robohash.org/voluptasdistinctioofficia.png?size=300x300&set=set1",
#         "gender": "Agender",
#         "phone_number": "+1-868 1-132-219-6472 x76354",
#         "social_insurance_number": "938654803",
#         "date_of_birth": "1986-01-07",
#         "employment": {
#             "title": "Product Construction Engineer",
#             "key_skill": "Confidence"
#         },
#         "address": {
#             "city": "Port Roger",
#             "street_name": "Ian Throughway",
#             "street_address": "756 Sylvie Mount",
#             "zip_code": "32478-9970",
#             "state": "North Dakota",
#             "country": "United States",
#             "coordinates": {
#                 "lat": 8.065438505838273,
#                 "lng": 95.61482818132123
#             }
#         },
#         "credit_card": {
#             "cc_number": "6771-8958-2389-0196"
#         },
#         "subscription": {
#             "plan": "Gold",
#             "status": "Pending",
#             "payment_method": "Alipay",
#             "term": "Full subscription"
#         }
#     },
#     {
#         "id": 7684,
#         "uid": "e69b18b1-ecd7-45f2-895d-eeea9279e91a",
#         "password": "DaCy3GOIWP",
#         "first_name": "Exie",
#         "last_name": "Tillman",
#         "username": "exie.tillman",
#         "email": "exie.tillman@email.com",
#         "avatar": "https://robohash.org/nequeliberoquia.png?size=300x300&set=set1",
#         "gender": "Genderfluid",
#         "phone_number": "+240 (806) 104-8952 x142",
#         "social_insurance_number": "956978340",
#         "date_of_birth": "1967-05-20",
#         "employment": {
#             "title": "National Hospitality Technician",
#             "key_skill": "Teamwork"
#         },
#         "address": {
#             "city": "Sanfordtown",
#             "street_name": "Tajuana Isle",
#             "street_address": "4625 Kilback Burg",
#             "zip_code": "92791",
#             "state": "Hawaii",
#             "country": "United States",
#             "coordinates": {
#                 "lat": -23.976114879745694,
#                 "lng": -79.59171324057827
#             }
#         },
#         "credit_card": {
#             "cc_number": "6771-8994-2981-0780"
#         },
#         "subscription": {
#             "plan": "Professional",
#             "status": "Blocked",
#             "payment_method": "Cheque",
#             "term": "Annual"
#         }
#     },
#     {
#         "id": 2515,
#         "uid": "5db1142c-2e32-4d10-b9cf-ce86ee6394a9",
#         "password": "j2NW6JzTfs",
#         "first_name": "Louis",
#         "last_name": "Swaniawski",
#         "username": "louis.swaniawski",
#         "email": "louis.swaniawski@email.com",
#         "avatar": "https://robohash.org/doloremdoloremvelit.png?size=300x300&set=set1",
#         "gender": "Polygender",
#         "phone_number": "+677 855-851-9250 x8749",
#         "social_insurance_number": "384601837",
#         "date_of_birth": "1962-02-05",
#         "employment": {
#             "title": "Central Specialist",
#             "key_skill": "Proactive"
#         },
#         "address": {
#             "city": "Gavinton",
#             "street_name": "Cassondra Wall",
#             "street_address": "4136 Hand Underpass",
#             "zip_code": "54574-5249",
#             "state": "New Hampshire",
#             "country": "United States",
#             "coordinates": {
#                 "lat": 22.23839947718399,
#                 "lng": -89.97008200017082
#             }
#         },
#         "credit_card": {
#             "cc_number": "6771-8920-8540-9047"
#         },
#         "subscription": {
#             "plan": "Silver",
#             "status": "Pending",
#             "payment_method": "Paypal",
#             "term": "Payment in advance"
#         }
#     },
#     {
#         "id": 1300,
#         "uid": "559abe32-114e-4526-a45d-c2d8bcc5d344",
#         "password": "OU2M7sZPxF",
#         "first_name": "Bulah",
#         "last_name": "Predovic",
#         "username": "bulah.predovic",
#         "email": "bulah.predovic@email.com",
#         "avatar": "https://robohash.org/ineaad.png?size=300x300&set=set1",
#         "gender": "Non-binary",
#         "phone_number": "+32 224.957.7238 x4249",
#         "social_insurance_number": "158922229",
#         "date_of_birth": "1962-11-28",
#         "employment": {
#             "title": "Investor Developer",
#             "key_skill": "Self-motivated"
#         },
#         "address": {
#             "city": "Port Kerry",
#             "street_name": "Freddie Landing",
#             "street_address": "992 Hegmann Groves",
#             "zip_code": "01477",
#             "state": "Michigan",
#             "country": "United States",
#             "coordinates": {
#                 "lat": -21.76884862079598,
#                 "lng": 28.51153708763229
#             }
#         },
#         "credit_card": {
#             "cc_number": "5514-5861-1886-7205"
#         },
#         "subscription": {
#             "plan": "Diamond",
#             "status": "Idle",
#             "payment_method": "Google Pay",
#             "term": "Monthly"
#         }
#     },
#     {
#         "id": 6973,
#         "uid": "9cebfd59-ee05-4a9d-9850-4f04cca0529a",
#         "password": "0ts6f14LJM",
#         "first_name": "Tomeka",
#         "last_name": "Douglas",
#         "username": "tomeka.douglas",
#         "email": "tomeka.douglas@email.com",
#         "avatar": "https://robohash.org/ametabfacilis.png?size=300x300&set=set1",
#         "gender": "Male",
#         "phone_number": "+357 1-208-142-0512",
#         "social_insurance_number": "212257323",
#         "date_of_birth": "1974-04-20",
#         "employment": {
#             "title": "Consulting Engineer",
#             "key_skill": "Networking skills"
#         },
#         "address": {
#             "city": "South Elenore",
#             "street_name": "Alphonso Mission",
#             "street_address": "126 Azalee Grove",
#             "zip_code": "40261",
#             "state": "Connecticut",
#             "country": "United States",
#             "coordinates": {
#                 "lat": 49.313550752155834,
#                 "lng": 23.01011543782161
#             }
#         },
#         "credit_card": {
#             "cc_number": "4905621629308"
#         },
#         "subscription": {
#             "plan": "Professional",
#             "status": "Blocked",
#             "payment_method": "Apple Pay",
#             "term": "Monthly"
#         }
#     }
# ]
