from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['organizations']
collection = db['organizations']
posts = db.posts

post = {"name": "Action Against Hunger", "address": "247 West 37th Street, 10th Floor, New York, NY 10018","phone": "877-777-1420","type": "cyclone", "about": "Working on the ground in Myanmar since 1994, Action Against Hunger / Action Contre la Faim (ACF) teams responded immediately with rapid assessments around Yangon and in the Ayeyarwaddy delta. Based on rapid assessments, ACF launched emergency operations in Yangon and Bogalay while flying reinforcements to the region to ensure a response in the south. Current programs: environmental clearing and clean-up; distributions of nutritional products (high protein biscuits), food (rice, oil, beans, lentils), and essential nonfood items (cooking and hygiene kits); distributions of water purifying tablets, pumps, and equipment for the provision of clean water. Next phase: rehabilitation and protection of water points and hygiene education; distributions of rations, cash, and/or vouchers depending on market accessibility. Donations can be made securely at http://support.actionagainsthunger.org/donate"}
posts.insert_one(post)

post = {"name": "ADRA International", "address": "12501 Old Columbia Pike, Silver Spring, MD 20904", "phone": "800-424-2372", "type": "cyclone", "about": "In a continued effort to assist the survivors of Cyclone Nargis, the Adventist Development and Relief Agency (ADRA) has committed at least $235,000 in emergency funds for immediate disaster relief, and is providing food assistance and medical supplies to communities in the hard-hit Irrawaddy Delta region in southern Myanmar. ADRA is currently accepting financial contributions to help the communities affected by this disaster. Donations can be made securely at http://www.adra.org/"}
posts.insert_one(post)


post = {"name": "Air Serv International", "address": "410 Rosedale Court, Suite 190, Warrenton, VA 20186", "phone": "866-428-2323", "type": "cyclone", "about": "Air Serv International is preparing to be a first responder to Myanmar disaster. With helicopters ready to deliver crucial supplies and relief workers to areas hardest hit in this devastated country, Air Serv is conducting a needs-assessment on how to deliver aid to the Myanmar people quickly and efficiently. As time is always an issue in responding to a disaster, Air Serv mobilized its Rapid Response Team the moment news broke about the events in Myanmar. Air Serv International is accepting gifts in kind of aircraft equipment, communications equipment, and fuel"}
posts.insert_one(post)

post = {"name": "American Friends Service Committee", "address": "1501 Cherry Street, Philadelphia, PA 19102", "phone": "888-588-2372", "type": "cyclone", "about": "The American Friends Service Committee is responding to the flooding in Myanmar with immediate assistance to those affected. AFSC also is committed to a long-term recovery that is flexible to the needs of the Burmese people, building on our ongoing partnerships with community groups and schools"}
posts.insert_one(post)

post = {"name": "American Jewish Joint Distribution Committee", "address": "132 East 43rd Street, New York, NY 10017", "phone": "212-687-6200", "type": "cyclone", "about": "JDC is collecting funds to assist the cyclone victims on a nonsectarian basis. JDC is now in contact with leaders from the local Jewish Community in Yangon and with other disaster relief partners in the region to determine an appropriate emergency response, one that reaches those who are not being served by others."}
posts.insert_one(post)
