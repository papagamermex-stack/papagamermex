module.exports = {
  layout: "post.njk",
  tags: "resenas",
  eleventyComputed: {
    permalink: function(data) {
      const slug = data.page.fileSlug.replace(/^\d{4}-\d{2}-\d{2}-/, '');
      return `/resenas/${slug}/index.html`;
    }
  }
};
