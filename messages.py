import telebot.formatting as frm

en = {} 
it = {}

# Welcome message
en['welcome_message'] = f"A very warm welcome, {'{}'} {'{}'}!\n\nI'm the {frm.hbold('Grill Valley bot')} 🤖 and I'm pleased to see you here. Hope you will stick around a {frm.hitalic('bit')} 😄.\n\nFirst of all.. {frm.hbold('Do you know Grill Valley?')}\n🔴 If not, here it is the {frm.hlink('aftermovie', 'https://youtu.be/1bTJatSOQb8')} of some event in a galaxy far, far away..\n🟢 If so, maybe you want to watch it for a blast from the past..\n\n\nMore specifically, it's a BBQ party 🔥 organized from and for {frm.hitalic('Computer Science students')} 💻.\nStill, anyone is always welcome. The final goal is a comfort place to eat 🍔, drink 🍻 and enjoy the life ☀️ together.\n\nIn the past we held Grill Valley 0, Grill Valley 1, Grill Valley 2 and Grill Valley Returns 🦇. Brace yourself, because in may 🗓️, the saga will continue with...\n\n\n {frm.hspoiler('Grill Valley 100')}\n\n\nNow, don't waste any time and follow us on:\n\n🛩️ {frm.hlink('Telegram', 't.me/grillvalley')}\n📷 {frm.hlink('Instagram', 'https://www.instagram.com/grillvalley')}\n\nAnd have a nice day!"
it['welcome_message'] = f"Un caldo benvenuto, {'{}'} {'{}'}!\n\nSono il {frm.hbold('Grill Valley bot')} 🤖 e sono davvero felice di vederti qui. Spero che tu rimanga per un po' 😄.\n\nPrima di tutto.. {frm.hbold('Conosci Grill Valley?')}\n🔴 Se la risposta è no, qui trovi l'{frm.hlink('aftermovie', 'https://youtu.be/1bTJatSOQb8')} di un evento in una galassia lontana lontana..\n🟢 Se la risposta è si, magari vuoi rivederlo per un tuffo nel passato..\n\n\nPiù nello specifico, si tratta di una grigliata 🔥, organizzata da e per gli {frm.hitalic('studenti di informatica')} 💻.\nIn ogni caso, tutti sono sempre benvenuti. L'obiettivo finale è un posto tranquillo, dove mangiare 🍔, bere 🍻 e godersi la vita ☀️ assieme.\n\nIn passato abbiamo organizzato Grill Valley 0, Grill Valley 1, Grill Valley 2 e Grill Valley Returns 🦇. Preparati, perchè a maggio 🗓️, la saga continua con...\n\n\n {frm.hspoiler('Grill Valley 100')}\n\n\nOra, non perdere altro tempo e seguici su:\n\n🛩️ {frm.hlink('Telegram', 't.me/grillvalley')}\n📷 {frm.hlink('Instagram', 'https://www.instagram.com/grillvalley')}\n\nA presto!"

# Help
en['help'] = f"So you want to know what I can do, which is actually quite reasonable.\nHere are the commands that you can launch to interact with me:\n\n{frm.hbold('General')}\n 🎬 /start : Start the bot. Display the 'welcome message' and learn some more information about Grill Valley\n ℹ️ /help : Display this message\n ⚠️❓ /faq : Display the FAQ section. Here are the serious and less serious answers to some typical Grill Valley related questions.\n\n{frm.hbold('Subscription')}\n 📝 /subscribe : Start the subscription process. I will guide you though it, using the next commands: they allow you to update your preferences for the party even in other moments. You can withdraw at any time.\n ⛔ /withdraw : Withdraw your subscription to the party. No further action needed.\n 🍺 /eating : Update your eating preferences and your food allergies/intolerances.\n ⚠️💰 /pay: Show all the useful information about the payment of your share. Until the payment, the subscription will be incomplete.\n 👮 /status : Discover the status of your subscription."
it['help'] = f"Dunque vorresti sapere cosa posso fare, che in effetti è una richiesta ragionevole.\nQuesti sono i comandi che puoi lanciare per interagire con em:\n\n{frm.hbold('Generali')}\n 🎬 /start : Avvia il bot. Mostra il 'messaggio di benvenuto' e scopri qualcosa di più su Grill Valley\n ℹ️ /help : Mostra questo messaggio\n ⚠️❓ /faq : Mostra la sezione FAQ. Qui troverai le più o meno serie risposte che abbiamo dato ad alcune domande tipiche su  Grill Valley.\n\n{frm.hbold('Registrazione')}\n 📝 /subscribe : Inizia la procedura di registrazione all'evento. Ti guiderò io, con i prossimi comandi: utilizzandoli potrai modificare le tue preferenze pure in un secondo momento. Puoi annullare l'iscrizione in qualsiasi momento\n ⛔ /withdraw : Annulla l'iscrizione alla festa. Non serve fare altro.\n 🍺 /eating : Aggiorna le tue preferenze alimentari ed eventuali allergie/intolleranze.\n ⚠️💰 /pay: Visualizza tutte le informazioni utili sul pagamento della quota di iscrizione. Fino al pagamento la registrazione sarà in uno stato incompleto. \n 👮 /status : Scopri lo stato della tua sottoscrizione."

# Status
en['status_registered'] = f"Ok {'{}'}, I have just checked your status.\n\nUsername: @{'{}'}\nStatus: 🟢🟢\nFood: {'{}'}\n\n\nYay! Can't wait to see you at the party!"
it['status_registered'] = f"Ok {'{}'}, ho appena controllato il tuo stato.\n\nUsername: @{'{}'}\nStato: 🟢🟢\nCibo: {'{}'}\n\n\nEvvai! Non vedo l'ora di vederti alla grigliata!"

en['status_not_registered'] = f"Ok {'{}'}, I have just checked your status.\n\nUsername: @{'{}'}\nStatus: 🔴🔴\n\n\nIf you want to join, you can always hit /subscribe"
it['status_not_registered'] = f"Ok {'{}'}, ho appena controllato il tuo stato.\n\nUsername: @{'{}'}\nStato: 🔴🔴\n\n\nNel caso tu voglia unirti, puoi sempre cliccare /subscribe"

# Register procedure
en['subscribe_user'] = f"What?\nYou finally decided to subscribe🎉?\n\nThis is a clever idea, {'{}'}.\nNow I am going to guide you through the steps of the subscription 💪.\nDon't worry, you can {frm.hbold('withdraw')} at any time, you just need to use the command /withdraw.\n\nFirstly, I peeked 🕵️ and I see that your full name is {'{}'}. Is that correct?"
it['subscribe_user'] = f"Cosa?\nHai finalmente deciso di iscriverti🎉?\n\nQuesta è davvero un'ottima idea, {'{}'}.\nAdesso ti guiderò nei vari passi del processo di iscrizione 💪.\nNon preoccuparti, puoi sempre {frm.hbold('ritirare')} l'iscrizione in qualsiasi momento, devi solo usare il comando /withdraw.\n\nTanto per cominciare, Ho sbirciato 🕵️ e vedo che il tuo nome completo è {'{}'}. E' corretto?"

en['name_yes_no'] = {"name_yes": "Yes ✅", "name_no": "No 🅾️"}
it['name_yes_no'] = {"name_yes": "Si ✅", "name_no": "No 🅾️"}

en['user_rename'] = f"Ok then 🧐, could you tell me you real name?"
it['user_rename'] = f"Ok quindi 🧐, puoi dirmi il tuo vero nome?"

en['subscribe_user_success'] = f"Perfect, you have been successfully registered as {'{}'} 🎈! I am so glad 🥳 that you are going to be one of us!\n\nI would like to remember you to join {frm.hlink('this telegram link', 't.me/grillvalley')}, as it is the place were all the useful news 🗞️ will be told first ⏰.\n\nNow, when you have a bunch of {frm.hitalic('spare seconds')} (yes, it takes just seconds!) you could tell us what your eating habits 🍴 are using the command /eating.\nC ya!"
it['subscribe_user_success'] = f"Perfetto, ti sei correttamente registrato come {'{}'} 🎈! Sono così felice 🥳 che tu sia uno dei nostri!\n\nVorrei anche ricordarti di unirti a {frm.hlink('questo link di telegram', 't.me/grillvalley')}, dato che è il posto dove tutte le informazioni importanti 🗞️ verranno dette prima ⏰.\n\nAdesso, quando hai qualche {frm.hitalic('secondo libero')} (si, ci vogliono solo dei secondi!) puoi dirci quali sono le tuo abitudini alimentari 🍴 usando il comando /eating.\nA presto!"

en['subscribe_user_failure'] = f"It failed!\nFor some reason it seems that you registration was unsuccessful. I honestly don't know why, but my shitty creator 💾👾 must have f**ked some code again.\n\nIt is a shame 😳, as I DEFINITELY want you on our party 🔥. Could you contact the admins 👯 and tell them what happend? (🤫 They will override me and subscribe you directly 😉)"
it['subscribe_user_failure'] = f"Errore!\nPer qualche ragione sembra che la tua registrazione non sia andata a buon fine. Sinceramente non so come mai, ma il mio scarso creatore 💾👾 deve aver sfan***ato qualcos'altro.\n\nÈ una vergogna 😳, anche perchè io ti voglio ASSOLUTAMENTE alla nostra grigliata 🔥. Riesci a contattare gli admin 👯 e dirgli cosa è successo? (🤫 Mi overrideranno e ti iscriveranno manualmente 😉)"

en['withdrawn_user'] = f"Oh.. that is.. some news 😔.\nI'm sad, that you are not going to partecipate, but I get it.\nThere are still people that think that there are things more {frm.hitalic('important')} (🤯) than Grill Valley.\n\nJokes apart, your registration has been withdrawn.\nBut if you change your mind 🤞 you can always get back on board using the same /subscribe command.\nHave a nice day, {'{}'}"
it['withdrawn_user'] = f"Oh.. questa è.. una notizia 😔.\nSono triste che tu non possa partecipare, ma lo capisco.\nCi sono ancora persone che credono che ci siano cose più {frm.hitalic('importanti')} (🤯) di Grill Valley.\n\nScherzi a parte, la tua registrazione è stata ritirata.\nMa se cambi idea 🤞 puoi sempre tornare a bordo usando il solito comando /subscribe .\nTi auguro una buona giornata, {'{}'}"

en['already_registered'] = f"Mmm.. It seems that you were already registered in our system.\nWhat do you need?"
it['already_registered'] = f"Mmm.. Sembra che tu sia già iscritto nel nostro sistema.\nDi cosa hai bisogno?"

en['not_registered'] = f"Mmm.. You are not registered in our system, so i didn't do anything 🤷.\n\nWould you like to /subscribe instead 😜?"
it['not_registered'] = f"Mmm.. Non sei registrato nel nostro sistema, quindi non ho fatto nulla 🤷.\n\nVorresti magari iscriverti con /subscribe 😜?"

# Eating
en['eating_preferences'] = f"Nice {'{}'}, time to update your eating preferences 🍽️.\n\nWhat do you want to eat at the party?"
it['eating_preferences'] = f"Bene {'{}'}, è il momento di aggiornare le tue preferenze alimentari 🍽️.\n\nCosa vuoi mangiare alla grigliata?"

en['eating_options'] = {"eating_meat": "Meat and everything 🍖🍗", "eating_vegetarian": "No meat, I am vegetarian 🚫🥩", "eating_vegan": "Fully vegan 🌱🌿"}
it['eating_options'] = {"eating_meat": "Carne e tutto il resto 🍖🍗", "eating_vegetarian": "Niente carne, sono vegetarian* 🚫🥩", "eating_vegan": "Completamente vegan 🌱🌿"}

en['eating_updated_success'] = f"Good {'{}'}, now I know what are you willing to eat at the party!\n\nNow tell me, do you have any {frm.hbold('food allergies/intolerances')} 🥛🧀🍞?\nI would like to know in order to offer you a safe party, were you can enjoy lightheaded."
it['eating_updated_success'] = f"Bene {'{}'}, adesso so cosa vuoi mangiare alla grigliata!\nnAdesso dimmi, hai qualche {frm.hbold('allergia/intolleranza alimentare')} 🥛🧀🍞?\nMi piacerebbe saperlo per offrirti una grigliata sicura, dove tu possa divertirti senza pensieri."

en['eating_updated_failure'] = f"It failed!\nFor some reason it seems that this transaction on the eating preferences was unsuccessful. I honestly don't know why, but my shitty creator 💾👾 must have f**ked some code again.\n\nCould you contact the admins 👯 and tell them what happend 🤫? "
it['eating_updated_failure'] = f"Errore!\nPer qualche ragione sembra che questa transazione sulle preferenze alimentari non sia andata a buon fine. Sinceramente non so come mai, ma il mio scarso creatore 💾👾 deve aver sfan***ato qualcos'altro.\n\nRiesci a contattare gli admin 👯 e dirgli cosa è successo 🤫?"

en['allergies_yes_no'] = {"allergies_yes": "Yes ✅", "allergies_no": "No 🅾️"}
it['allergies_yes_no'] = {"allergies_yes": "Si ✅", "allergies_no": "No 🅾️"}

en['user_allergies'] = f"Ok then 🧐, could you tell me your food allergies/intolerances?"
it['user_allergies'] = f"Ok quindi 🧐, puoi dirmi il le tue allergie/intolleranze alimentari?"

en['update_food_allergies_success'] = f"Very well. I have updated your intolerances as required.\nNow your process of subscription is completed 😋.\n\nI feel that you might want to know a little more. Here are some commands, which are not mandatory, that you can use to explore this event a little more.\n\n - /volunteers : to discover a little bit about the 'behind the scenes' of this party and also consider to contribute.\n - /notes : To suggest ideas, criticisms, activities... Anything you would like to see that day. Everything will be considered and if possible realized, in order to make everyone feel in a comfortable and enjoyable place"
it['update_food_allergies_success'] = f"Molto bene. Ho aggiornato le tue intolleranze come richiesto.\nOra il tuo processo di sottoscrizione è completato 😋.\n\nCredo però che tu voglia sapere qualcosina di più. Qui trovi alcuni comandi, non obbligatori, che puoi usare per esplorare un po' di più questo evento.\n\n - /volunteers : Per scoprire qualcosa sul 'dietro le quinte' di questa grigliata e considerare anche di dare il tuo contributo.\n - /notes : Per suggerire idee, critiche, attività... Qualsiasi cosa ti piacerebbe vedere qul giorno. Tutte le proposte verranno considerate e dove possibile realizzate, in modo da far sentire tutti a proprio agio."

en['update_food_allergies_failure'] = f"It failed!\nFor some reason it seems that this transaction on the food allergies/intolerances was unsuccessful. I honestly don't know why, but my shitty creator 💾👾 must have f**ked some code again.\n\nCould you contact the admins 👯 and tell them what happend 🤫? "
it['update_food_allergies_failure'] = f"Errore!\nPer qualche ragione sembra che questa transazione sulle allergie/intolleranze alimentari non sia andata a buon fine. Sinceramente non so come mai, ma il mio scarso creatore 💾👾 deve aver sfan***ato qualcos'altro.\n\nRiesci a contattare gli admin 👯 e dirgli cosa è successo 🤫?"

# Generic messages
en['unknown_command'] = f"I'm truly sorry, but I'm not able to understand what you require. Are you sure that you sent the message to the right person? (which I am not, since I'm a bot)"
it['unknown_command'] = f"Mi spiace, ma non riesco a capire di cosa tu abbia bisogno. Sicuro di aver inviato il messaggio alla persona corretta? (che non posso essere io, visto che sono un bot)"