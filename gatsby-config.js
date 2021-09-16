module.exports = {
  plugins: [
    {
      resolve: `gatsby-theme-garden`,
      options: {
        contentPath: `${__dirname}/content/`,
        rootNote: `/Lịch Sử Việt Nam`,
      },
    },
  ],
  siteMetadata: {
    title: `Digital garden`,
  },
}
