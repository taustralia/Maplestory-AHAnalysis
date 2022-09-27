# Maplestory-AHAnalysis

TL;DR: A MapleStory Auction House companion to scrap historical sales data and store into a mySQL database for further statistical analysis and data visualization

## **Table of Contents**

[Background](#background)

[Purpose and Methodology](#purpose-and-methodology)

1. [Data Extraction](#data-extraction)
2. [Database Setup](#database-setup)

[How to Use](#how-to-use)

[Future Considerations](#future-considerations)

[Sample Results](#sample-results)

### **Background**

> MapleStory is a free-to-play side-scrolling MMORPG created in 2003. In this game, players are able to travel the "Maple World" defeating monsters and developing their characters' skills and abilities. Players can interact with others in many ways, including chatting and trading. Groups of players can also band together in parties to hunt monsters/bosses and share rewards, and can also form guilds to interact more easily with each other.

*excerpt from* [Maplestory Wiki Page]https://en.wikipedia.org/wiki/MapleStory

### **Purpose and Methodology**

I've been playing MapleStory in many iterations for almost 15 years. One of the many ways I found personal enjoyment while playing was through the ability to earn virtual money within the game. The virtual currency, denoted as a *meso* within the game, was used to trade goods between players and ultimately buy further upgrades to improve your character.

Around 2013, I started producing forum posts and eventually YouTube videos to document my money making process alongside with the improvement of my character. In order to keep up with market trends, I often spent hours scouring the *Free Market*  (the area in game where players could list their items for sale) and documenting information about the items sold. Things like item name, item price, amount sold and the date sold were the typical parameters I limited myself to. Using this data, I was able to identify key selling items and overall monitor price fluctuations using simple graphs and pivot tables in Excel. Based on the resultant analysis, I'd try to source these hot selling items for discounted prices and aim to sell at market price in order to generate revenue. Despite this process of manual data mining being quite tedious, I was able to keep up with this methodology until the developers of the game removed the Free Market and instead replaced it with the *Auction House*. Through the Auction House, players are still able to sell items; however, instead of having to physically go an visit a player's store through the Free Market, the items were all congregated in one place. 

It was due to this aggregation of data that this project was created. It became far too time consuming to manually data mine and this was, in turn, decreasing my enjoyment of the game. Because I was already comfortable with the data analysis component on a smaller scale, I thought it would be a great idea to create a program that automatically takes screenshots that were taken from the Auction House and using OCR (Optical Character Recognition) libraries to convert the images into text then eventually have that text automatically collected in a SQL database. I knew this project might end up being a bit expansive so I decided to split it into two main phases:

#### 1. Data Extraction

In this phase, the main focus was developing the script that would automatically convert the raw screenshots taken in-game into text output. This part including multiple components such as optimizing pytesseract, the image OCR library selected for this project, and pre-cleansing the data to allow for an easier time when manipulating this data down the line in the database. 

#### 2. Database Set-up

To be added after implementation.

### **How to Use**

To be added later.

### **Future Considerations**

To be added later.

### **Sample Results**

To be added later.

