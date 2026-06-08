const Parser = require('rss-parser');
const parser = new Parser();

module.exports = async function() {
  const feedUrl = 'https://anchor.fm/s/4fab7d50/podcast/rss';
  
  try {
    const feed = await parser.parseURL(feedUrl);
    
    // Obtener los últimos 5 episodios
    const latestEpisodes = feed.items.slice(0, 5).map(item => {
      // Extraer datos útiles
      let summary = item.contentSnippet || item.content || '';
      summary = summary.replace(/(<([^>]+)>)/gi, ""); // Strip HTML
      
      return {
        title: item.title,
        link: item.link,
        pubDate: item.pubDate,
        summary: summary.substring(0, 150) + '...',
        enclosure: item.enclosure ? item.enclosure.url : '',
        duration: item.itunes && item.itunes.duration ? item.itunes.duration : 'N/A'
      };
    });
    
    return latestEpisodes;
  } catch (err) {
    console.log("Error fetching podcast RSS:", err);
    return [];
  }
};
