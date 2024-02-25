import axios from 'axios';
import * as cheerio from 'cheerio';

const fetchPricingInfo = async () => {
  try {
    const { data: htmlText } = await axios.get('https://openai.com/pricing');
    const $ = cheerio.load(htmlText);

    const allModelLabels = $('tr.border-b.border-secondary');
    const allModelValues: cheerio.Element[][] = [];

    allModelLabels.each((_, element) => {
      const spanText = $(element).find('span').text();
      if (!['Input', 'Output', 'Model', 'Training', 'Input usage', 'Output usage', 'Price', 'Quality', 'Resolution'].includes(spanText)) {
        const models = $(element).find('span.f-body-1');
        if (models.length > 0) {
          const modelValues = models.map((_, model) => $(model)).get();
          allModelValues.push(modelValues);
        }
      }
    });

    allModelValues.forEach((model) => {
      // Assuming i[1] is to print the second span in each tr element
      // Adjust the index based on actual HTML structure if needed
      console.log($(model[1]).text());
    });
  } catch (error) {
    console.error('Error fetching pricing info:', error);
  }
};

fetchPricingInfo();
