module.exports = function(eleventyConfig) {
  // Passthrough copy for static assets
  eleventyConfig.addPassthroughCopy("images");
  eleventyConfig.addPassthroughCopy("admin");
  eleventyConfig.addPassthroughCopy("_redirects");

  // Add a simple date filter since Nunjucks doesn't have one built-in
  eleventyConfig.addFilter("date", function(dateObj, format) {
    if (!dateObj) return "";
    return dateObj.toISOString().split('T')[0];
  });

  return {
    dir: {
      input: ".",
      includes: "_includes",
      output: "_site"
    }
  };
};
