<h1>Executive Summary</h1>

In this report, we look at the leaked papers published by The International Consortium of Investigative Journalists (ICIJ). The database is the amalgamation of 4 separate leaks, namely, The Panama Papers, The Bahamas Papers, The Paradise papers and Offshore Leaks Papers. From this huge trove of information available to us, we analyse the data from 2 perspectives, namely the Macro Approach and the Micro Approach. Through this two-pronged approach, we derived meaningful insights into the dataset and identified the key players as well as the community associated with it from the dataset. 

In the Macro Approach, we identified the Tax Havens as well as Financial Hubs in the ICIJ Database. Armed with this information, we shifted our focus towards the Micro Approach and found the important firms that facilitate the creation of off-shore entity es around the world. We also delved into the affairs of the Duchy of Lancaster, who is the Queen of England, as a case example of how off-shoring of the elite rich is done.

As mentioned by Barack Obama,

*"It's not that they're breaking the laws," he said, "it's that the laws are so poorly designed that they allow people, if they've got enough lawyers and enough accountants, to wiggle out of responsibilities that ordinary citizens are having to abide by."*

<h1>Introduction </h1>

The Paradise Papers, Panama Papers, Bahamas Leaks and the Offshore Leaks are all separate leaks that form the ICIJ Offshore Leaks database. Almost 520,000 offshore entities have been revealed in this investigation database. 

Prior to this database, these companies and trusts incorporated in tax havens, as well as the people responsible, were kept under the cloak of secrecy. With this database, we are even able to see the real owners of these complex structures. More than 440,000 names of people and companies have been revealed. The database has a disclaimer that we should confirm the identities of any individuals or entities located in the database based on the given address or other information that can identify them. 

On 15 April 2016, ICIJ has published a huge database detailing the confidential financial information on the offshore entities as well as the relationship of these entities with the famous and powerful people in the world. While offshore business entities are legal and can be used for legitimate reasons, the purpose of some are more dubious and darker. In this report, we look at the information available to us from an objective point of view and aim to derive insights from this.

<h1>Business Problems</h1>

<h2>Question: Which countries are the Tax Havens (Key Players)? </h2>

We would like to know which countries serve as the world’s tax havens. These countries could serve as actual “offshore-friendly” countries, or as financial hubs  who have the infrastructure to facilitate these offshore legal complexities and transactions. 

<h2>Question: What are the communities among the key players? </h2>

After obtaining the tax havens, we would like to delve a bit deeper into who are the Officers that operate around these tax havens. This would be useful insight into which companies / personnel are largely responsible for such offshore activities. 

<h1>Data Exploration </h1>
<h2>Data contained in the Paradise Papers: </h2>
- Officer: A person or company who plays a role in an offshore entity, such as beneficiary, director, or shareholder. The relationships shown in the diagram are just a sample of all the existing ones.

- Intermediary: Go-between for someone seeking an offshore corporation and an offshore service provider, usually a law-firm or a middleman that asks an offshore service provider to create an offshore firm for a client.

- Entity The offshore legal entity. This could be a company, trust, foundation, or other legal entity created in a low-tax jurisdiction.

- Address: Postal address as it appears in the original databases obtained by ICIJ.

- Other: Additional information items.

![Overview_Image](https://github.com/rickyken90/ICIJ-Graph-Analysis/blob/master/Images/overview_image.jpg)<br />
Figure 1 - Relationship between the different nodes<br />

Test |Bahamas Papers | Offshore Leaks | Panama Papers | Paradise Papers
------------ | ------------- | ------------- | ------------- | -------------
Total No. of Relationships |249,191 | 561,393 | 674,103 | 364,475
Entities                   |175,888 | 105,517 | 213,635 | 24,957
Intermediary               |541     | 9,527   | 14,111  | 186
Officer                   | 25,262  | 107,191 | 238,403 | 77,012

Table 1- Size of the ICIJ Database
Figure 1 and Table 1 show the overall view of the dataset. From the viewpoint of the dataset, it is deemed that exploring the dataset together is computationally intensive and not viable.
As such, we do a two-prong approach to draw meaningful insights into the data namely the Micro Approach and the Macro Approach.

For the Marco approach, more focus is placed on the Entities and Countries. All the Entities datasets will be combined together, and Feature Engineering is done to extract out the information needed.
Feature Engineering

We perform Feature Engineering on the Entities Dataset.

No	| Name of Column	| Remarks
------------ | -------------| -------------
1	| 'name'	| Name of the Foreign Entity
2	| 'countries'	| Country it operates in
3	| 'jurisdiction_description'	| Country which has Legal Jurisdiction over the Entity
4	| 'incorporation_date'	| 
5	| 'inactivation_date'	| 
6	| 'address'	| Address of Entity

Table 2 - Feature Engineering<br />
We took out the relevant information as shown in the table above. With these columns, we check for duplicate records and remove the duplicates. Next, we inspect the values of each column. It is noted that there are missing or erroneous values in the dataset. These are not relevant in our analysis and are removed.  After which, we count the number of linkages between the countries and labels as weights. Table 2 shows the sample of the output after Feature Engineering. Through manual inspection, it is found that both the source and the target can be of the same country. As such, it has been removed in a bid to provide a more accurate analysis.

Target	|Source|	Weight
------------ | -------------| -------------
British Virgin Islands	|Hong Kong	|27,228
British Virgin Islands|	Switzerland	|19,650
Panama	|Switzerland	|11,590
British Virgin Islands	|Jersey	|10,467
Panama	|Luxembourg	|5,584

Table 3 - Sample of the output

<h1>Graph analysis</h1>
<h2>Key Player Detection</h2>
<h3>Detecting the key countries (Macro Approach)</h3>

To identify the key countries that are involved in the database, two algorithms namely, PageRank algorithm and Betweenness Centrality algorithm are used to detect the key players. PageRank Algorithm…… Betweenness Centrality algorithm seeks out the middle man of the graph. It identifies the key nodes that facilitates the transfer of information to other nodes. PageRank is an algorithm to calculate the importance of the nodes in the network and rank them accordingly. Both identify the key players in the graph with different objectives in mind. We use the algorithms available in NEO4J to calculate out the scores. The results are as shown in Table 4 below.

No           |	Weighted PageRank	|         |            |	Betweenness Centrality
------------ | -------------| -------------| -------------| -------------
|	Country	| Score	||	Country	| Centrality
1|	British Virgin Islands	|34.08	|	Panama	|1058.99
2	|Panama|	32.59	|	British Virgin Islands	|581.49
3|	Bahamas|	22.88	|	Bahamas	|460.25
4|	Seychelles|	8.02	||Hong Kong	|419.16
5|	Niue	|6.01		|Singapore|	163.47
6|	Nevada	|2.00		|Seychelles|	120.10
7|	British Anguilla|	1.94	|	New Zealand|	28.13
8|	Samoa	|1.87		|United Kingdom	|24.00
9|	Hong Kong	|0.66	|	Belize|	20.79

Table 4- Results of Weighted PageRank and Betweenness Centrality
From Table 3, we can see that the results differ for both algorithms. In Weighted PageRank, all the top 8 countries are labelled as Tax Havens save for Nevada. Nevada can be considered an outlier for it has unique tax rules within US. As such, we can see that PageRank is very good at identifying all the Tax Havens around the world. 

For Betweenness Centrality Algorithm, it identifies the Key Countries who are famous for their financial services. Hong Kong and Singapore are famous for their wealth management in Asia. In 2018, Hong Kong’s wealth management assets has surpassed 1 trillion. [10] London (UK) is also famous for their wealth management services. They are known as financial centres or hubs.

The 2 question naturally comes about. 

What are the characteristics of a Tax Haven?
What are the characteristics of a Financial Centre?

We choose to examine the Tax Havens top countries in the above tables: Panama, Bahamas and the British Virgin Islands from North America, Samoa from Oceania. These countries share the below characteristics [2, 3, 4, 5, 6]:
•	These countries offer tax and business friendly laws for foreign investors and have low or even non-existent taxes for foreign individuals and companies. 
•	These countries also have legislations in place to ensure financial records are private and financial institutes are not required to provide access to personal data about individuals. 
•	These countries are small, have a stable government and their government use the small franchise tax received from these foreign companies to cultivate new streams of national revenue.
Many of these companies are managed by law firms like Mossack Fonseca [8], Appleby [7] etc. which are based out of Financial Centres. Due to the regulations and the above reasons, the law firms are not required to keep records of any transactions. These factors together lead to these countries being classified as tax havens.

Detecting Key officers (Micro Approach)

We have taken note of the Tax Havens and the key characteristics that comes along with the countries. Therefore, it will be prudent to go deeper into the analysis of these countries and obtain more information on the Key Firms and the communities associated with them. We will be looking at the following countries, namely British Virgin Island and China.

As mentioned in the introduction, an officer plays an important role in an offshore entity by being a shareholder/director of the same company. With this information, we can create a social network of officers all around the world, However, due to the scale of the social network being created, we have only created the social links for the countries named above.

It is assumed that the officers who are related to the same entity have some form of contacts with one another. The relationship created will be bi-directional and one of the officers will be within the stated country as shown in Figure 2.












We run PageRank with the nodes being the Officers and the links being the newly created social link “COMMON_INVESTMENTS_COUNTRY” on China and British Virgin Island. Table 5 denotes the results obtained.

PageRank of China		PageRank of British Virgin Island
Officer	Score		Officer	Score
"Portcullis TrustNet (Samoa) Limited"	1714.72		"Trustcorp Limited"	1267.16
"MOSSFON SUBSCRIBERS LTD."	766.51		"Acticorp Limited"	652.57
"Execorp Limited"	558.46		"Execorp Limited"	450.15
"D TIMOTHY PINKNEY & NANCY D PINKNEY JT TEN"	167.28		"Sherper Limited"	176.80
"PHILIP GAROON"	132.12		"Burns - Michael J"	158.80
"CHEN Ching-Wen"	128.05		"Commonwealth Trust Limited"	117.35
"Reid Services Limited - Cayman"	126.74		"Mermeden Ltd"	93.90
"Sharecorp Limited"	85.35		"Mills - Judith A"	77.046
"Stockcorp Limited"	48.93		"Yicko Skyford Capital Limited"	75.54
"PricewaterhouseCoopers - Hong Kong"	39.17		"Valinco Investments Limited"	72.90
Table 5- Page Rank of China and BVI
Research online reveals that Portcullis TrustNet is in fact a Singapore-based law firm. Based on the website, it offers services such as Trustee, Foundations as well as fund administration across the world. From ICIJ Database, it has 280 thousand entities connected to the company across the whole world. In 2013, it was one of the largest Wealth Advisory companies in Asia. Therefore, it comes with no surprises that Portcullis TrustNet is one of the key firms in helping high net-worth individuals, family offices etc. from China to set up offshore entities across the world. [11] This is the same for firms such as Trustcorp Limited, Acticorp Limited, and Execorp Limited where the firms sell financial and wealth management services to high net worth individuals. One of Execorp Limited subsidiary, Oxel Systems Pte. Ltd, is in the business of supply and sale of chips for use in personalised electronic identification cards or “smart cards”. Oxel System was involved in legal battle with PT. Sandipala Arthaputra in regards of “E-KTP Cards” (electronic ID) tender for Indonesian population [12]. Mr Andi Bharata Winata (“Mr Winata”) was Oxel’s Sales and Marketing Representative in Indonesia. He is the son of Tommy Winata, one of richest businessman in Indonesia [13][14]. This tender project was embroiled in corruption case controversies which involved highly powerful figures, including the Indonesian Head of House of Representative, Setya Novanto [15]. 

Community detection
Detecting communities from interactions between countries

The data that show the connection between the countries is used as the initial data for the community detection. We use Gephi for this part of the analysis. We want to observe the communities that are created based on the countries that interact with Singapore in the data. We filter the data by keeping countries that are connected to Singapore and their connections by using an Ego network query with the pattern set to Singapore and the depth set to 1. 

 
Figure 3 Components extracted for countries connected to Singapore (pink, yellow and green nodes)
Gephi uses the community detection approach as mentioned in the algorithm “Fast unfolding of communities in large networks” [9]. A modularity score of 0.087 is obtained and 3 communities are detected when the algorithm is run on the filtered graph. Selected countries that form the communities after the algorithm is run is mentioned in the below table also.

Community 1	Community 2	Community 3
Singapore	Malaysia	Taiwan
Hong Kong	Bahamas	Seychelles
Indonesia	Mauritius	Samoa
Switzerland	Canada	Netherlands
Cook Islands	British Virgin Islands	Liechtenstein
Table 6 - Countries part of the communities (only 6 shown for each)
As the above table shows each community has some major tax havens – Switzerland and Cook Islands for the first community, Bahamas and British Virgin Islands for the second community and Samoa and Seychelles from the third community. Hong Kong and Singapore in the first community are influential intermediaries as many firms that specialize in setting up of offshore entities are based out of these countries. 
From Singapore’s perspective, it can be said that wealthy individuals and firms from Indonesia utilize the services of intermediaries in Singapore and Hong Kong to set up their shell establishments in the tax havens of Switzerland and the Cook Islands. 
It needs to be noted that the modularity of the communities generated using the algorithm is low at a value of approx. 0.09. Based on the findings different tax havens have different tax laws which means that countries like Luxembourg are favoured for their patent tax benefits while those like Panama are favoured for their income tax benefits [16]. Since companies across most countries in the world would have multiple requirements to minimise the tax payable in their home countries, the interconnections between the tax havens and hence the communities are high, which leads to a low modularity score.

A Royal Community Case Study: The Duchy of Lancaster 

As such, we look from another perspective to find out the communities from the database. 
Another news from the Paradise Papers was that the Queen of England has various off-shoring outlets. We can gain useful insights even by using simple but powerful queries. By finding shared entity relationships between officers named “Duchy of Lancaster” (The Queen of England) and other officers, we can obtain the graph below. 

 
Figure 4 Network of Queen of England

Note that “The Duchy of Lancaster” has a company “Jubilee Absolute Return”, which is based in Bermuda. There are 4 other officers which are officers of “Jubilee Absolute Return”, namely:  Sutherland – Linda M, Waters Jnr. – Col. Sumner Horton, Fauchier Partners International Ltd. and RSM Robson Rhodes LLP. Of these 4, 3 of them are based in Bermuda, and registered at Head Office, 6 Front Street in Bermuda. Of the 3 based in Bermuda, Sutherland is an officer of numerous companies as well. The revelation is that these companies are almost all located at the same location, Head Office, 6 Front Street in Bermuda, which is probably why this warrants an investigation.

  

Other Stories 
There are many other cases discovered by journalists over the years from the data. Few of the prominent ones –
•	U.S.A. – President Donald Trump and his cabinets https://projects.icij.org/paradise-papers/the-influencers/#/_ga=2.12709621.39699692.1541000890-1782747271.1540287014 
•	Canada – Former PM - Paul Martin and CSL Group https://offshoreleaks.icij.org/stories/paul-martin 
•	Jordon – Queen Noor Al Hussein 
https://offshoreleaks.icij.org/stories/noor-al-hussein 
•	Russia – a close friend of Putin 
https://offshoreleaks.icij.org/stories/sergey-roldugin 
With closer investigation on every entity and comparison across the years it will be possible to observe more interesting insights.
Further Improvements
We were able to detect communities in subgraphs using keyword retrieval but found it difficult to run current algorithms with increase in the scale of data. Some of the algorithms like Neumann Community Detection hanged when running for the overall graph with over 500K nodes and 2M edges. We can try adopting distributed variants of such algorithms in future.

There exists an alternative of creating a custom algorithm to iterate through top scored ‘seed’ nodes (Officers / Countries) and recursively expand subgraph up to N neighbours. This following a single machine approach requires more RAM to scale up.

Another future consideration is to detect cycles in the graph to know if any community keeps continuously circulating money internally within its own entities.
Conclusion
We analysed the leaked papers published by The International Consortium of Investigative Journalists and identified the key players and the communities created around them. Key players were identified from two perspectives – the Macro Approach and the Micro Approach. In the Macro Approach, we identified certain countries that serve as Tax Havens. From the Micro Approach we discovered firms that act as intermediaries and pave the way to move money out to these tax havens. Having such key players as the centre figure, we were able to traverse their neighbours and expand into communities on both country and individual firm  level. We also delved into the affairs of the Duchy of Lancaster, owned by the Queen of England, as a case example of how offshoring by the elite rich is done. Finally, emerging stories focusing on prominent leaders from other countries from this huge database were briefly discussed.

Disclaimer
Through this report, we aim to obtain a deeper understanding of the accumulated Leaked Database and all insights obtained here are meant for research purpose only. As such, no part of this report is to be reproduced for any other purpose other than research. 

References

[1] https://neo4j.com/blog/analyzing-panama-papers-neo4j/
[2] https://www.theatlantic.com/business/archive/2016/04/panama-tax-haven/476766/
[3] https://www.investopedia.com/ask/answers/060516/why-bahamas-considered-tax-haven.asp
[4] https://www.businessinsider.sg/british-virgin-islands-a-tax-haven-or-legitimate-business-hub-2017-6/?r=UK&IR=T
[5] https://www.investopedia.com/ask/answers/060716/why-singapore-considered-tax-haven.asp
[6] http://pacificguardians.org/blog/2015/02/15/samoa-ranked-no-1-as-worlds-most-secretive-tax-haven-potential-for-more-investors/
[7] https://www.applebyglobal.com/about/
[8] http://mossfonmedia.com/
[9] Blondel, V. D., Guillaume, J. L., Lambiotte, R., & Lefebvre, E. (2008). Fast unfolding of communities in large networks. Journal of statistical mechanics: theory and experiment, 2008(10), P10008.
[10] https://international-adviser.com/hong-kong-wealth-management-assets-hit-1trn/
[11] https://uk.reuters.com/article/uk-portcullis-wealth-insight/insight-a-singapore-wealth-manager-under-fire-amid-crackdown-idUKBRE9510E920130603
[12] https://www.supremecourt.gov.sg/docs/default-source/module-document/judgement/-2017-sghc-102-pdf.pdf
[13] https://en.tempo.co/read/news/2017/05/18/055876437/E-KTP-Trial-Paulus-Tanos-Admits-He-Received-Death-Threats
[14] https://www.forbes.com/lists/2006/80/06indonesia_Tomy-Winata_RSXG.html
[15] https://www.theguardian.com/world/2017/nov/16/top-indonesian-politician-corruption-case-missing
[16] http://nomadcapitalist.com/2017/09/15/low-tax-countries-intellectual-property-ultimate-guide/





