# ChatGDP

## Inspiration
Have you ever unknowingly spent extra money just trying to understand how an API works? Well, we definitely have. During one of our group member's research projects, he unknowingly spent over $100 using an API key that didn't belong to him. This is where ChatGDP comes in.

## What it does
ChatGDP is a VSCode extension that utilizes HTTP Requests and displays a live price of your OpenAPI's API usage in a friendly window. All you need to do is run the code; we'll do the rest for you.

## How we built it
ChatGDP runs on 4 main components: Web Scraping, Databasing, Network Monitoring, and Extension.

Our Web Scraping is powered by BeautifulSoup, to parse through OpenAI pricing website and extract key pricing information. Our Databasing is built on SQL, where our web scraping data is stored. Our Network Monitoring runs through a mixture of network monitoring with pyShark and API redirecting with Flask. Finally, our extension is run mainly on typescript, where we use a mixture of front end technologies like HTML, CSS, and JS to receive data from SQL and display it.

## Challenges we ran into
During the development of our ChatGDP, we encountered significant challenges in API tracking due to compatibility issues. Moreover, establishing connections with the SQL database and its integration with the front-end presented considerable obstacles, demanding innovative solutions to ensure seamless operation and user experience.

## Accomplishments that we're proud of
Our most significant achievement was the successful integration of diverse technologies—network monitoring, web scraping, front-end, and back-end development—into a single application. This multifaceted approach provided us with valuable insights into the complexity and interdisciplinary nature of real-world software projects, showcasing our ability to navigate and combine various technological domains effectively.

## What we learned
Throughout the project, we acquired skills in developing a Visual Studio Code extension, mastered web scraping techniques, and learned to monitor network traffic utilizing PyShark, significantly enhancing our technical proficiency and practical knowledge in software development.

# What's next for ChatGDP
Our goal is to expand our usage for further websites, not just OpenAI. By potentially utilizing the power of generative AI and its capability of parsing through HTML, standardizing and extracting pricing information for a bunch of API's would heavily grow ChatGDP's helpfulness for developers.
