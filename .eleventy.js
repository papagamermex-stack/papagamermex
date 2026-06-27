module.exports = function(eleventyConfig) {
  // Passthrough copy for static assets
  eleventyConfig.addPassthroughCopy("images");
  eleventyConfig.addPassthroughCopy("admin");
  eleventyConfig.addPassthroughCopy("_redirects");
  eleventyConfig.addPassthroughCopy("robots.txt");

  eleventyConfig.addFilter("date", function(dateObj, format) {
    if (!dateObj) return "";
    try {
      const d = new Date(dateObj);
      return d.toISOString().split('T')[0];
    } catch (e) {
      return dateObj;
    }
  });

  return {
    dir: {
      input: ".",
      includes: "_includes",
      output: "_site"
    }
  };
};
