# Jenkins job for generating html file for graphql API
This Jenkins job generates graphql API description into one single html file (index.html) which contains styles and scripts in its head.

It takes as parameters:
 - introspection url
 - server url
 - title
 - description

It uses spectaql and can be customized by updating theme/stylesheets/custom.scss file.
