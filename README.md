## Life++
The web app focuses on providing a secure online storage for the user’s medical records. The user will sign in to his account and access a dashboard of his medical records. The user will submit a photo of the physical prescription which he/she receives from the doctor. Alternatively , the doctor too can submit a photo of the prescription he/she prescribed to the user. Once any user uploads a photo of the prescription , the app performs optical character recognition and extracts text from it.

To ensure the incorruptibility of the document , a hash of the document is generated and is logged in a blockchain. The blockchain ensures that the hash of the document cannot be tampered with in any condition. When the user requests for the document again, the app matches the hash of the document present in its database with that in the blockchain. If they are found to be same, it means the article was not tampered with.

### Features:
-   Transforms image of prescription into text
-   Ensures incorruptibility of stored document by pushing hash of text in blockchain.
-   Can recognise pneumonia in common X-Rays.

### Technologies used:

1.  Django framework (for backend)
2.  Web3.py (to talk with the blockchain)
3.  Ganache (A local blockchain based on Ethereum)
4.  Solidity (To create Smart Contracts)
5.  Tesseract.js (OCR)
6.  Keras (Machine learning models)
7.  SQLite (Database)

### Activity Diagram

<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/activity.PNG">

### Screenshots of the application

<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/1.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/2.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/3.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/4.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/7.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/8.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/11.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/9.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/10.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/12.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/13.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/18.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/14.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/6.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/5.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/15.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/17.png">

#### Ganache 
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/19.png">
<img src = "https://github.com/shlokashah/life_plus_plus/blob/master/docs/20.png">

