module.exports = {
  layout: "post.njk",
  tags: "para_padres",
  eleventyComputed: {
    permalink: function(data) {
      const slug = data.page.fileSlug.replace(/^\d{4}-\d{2}-\d{2}-/, '');
      return `/para-padres/${slug}/index.html`;
    }
  }
};
