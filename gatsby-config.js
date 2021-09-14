module.exports = {
  plugins: [
    {
      resolve: `gatsby-theme-garden`,
      options: {
        contentPath: `${__dirname}/content/`,
        rootNote: `/Enter the garden`,
      },
    },
  ],
  siteMetadata: {
    title: `Digital garden`,
  },
}
