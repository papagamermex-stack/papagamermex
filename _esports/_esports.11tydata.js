module.exports = {
  layout: "post.njk",
  tags: "esports",
  eleventyComputed: {
    permalink: function(data) {
      const slug = data.page.fileSlug.replace(/^\d{4}-\d{2}-\d{2}-/, '');
      return `/esports/${slug}/index.html`;
    }
  }
};
