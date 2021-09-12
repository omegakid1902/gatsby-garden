module.exports = {
  plugins: [
    {
      resolve: `gatsby-theme-garden`,
      options: {
        contentPath: `${__dirname}/content`,
        rootNote: `/hello`,
      },
    },
  ],
  siteMetadata: {
    title: `Site title`,
  },
}
