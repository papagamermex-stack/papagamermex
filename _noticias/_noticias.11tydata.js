module.exports = {
  layout: "post.njk",
  tags: "noticias",
  eleventyComputed: {
    permalink: function(data) {
      const slug = data.page.fileSlug.replace(/^\d{4}-\d{2}-\d{2}-/, '');
      return `/noticias/${slug}/index.html`;
    }
  }
};
