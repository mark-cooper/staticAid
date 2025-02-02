// builds lunr
// (with gratitude to https://github.com/katydecorah/katydecorah.github.io/blob/master/js/lunr-feed.js and http://rayhightower.com/blog/2016/01/04/how-to-make-lunrjs-jekyll-work-together/)

const index = lunr(function () {
  this.field('identifier')
  this.field('title')
  this.field('display_string')
  this.field('url')
  this.field('record_type')
  this.field('creator')
  this.field('singlepart_notes')
  this.field('multipart_notes')
  this.field('subjects')
  this.ref('href')
})

const searchData = $.getJSON('/search_data.json')
searchData.then(function (data) {
  $.each(data, function (i, value) {
    index.add(value)
  })
})

$(document).ready(function () {
  $('#search').submit(function (event) {
    event.preventDefault()
    const results = new bootstrap.Offcanvas($('#searchResults'))
    const resultsText = $('#searchResults .offcanvas-body')
    const query = $('#query').val()
    const result = index.search(query)
    resultsText.empty()
    resultsText.append(`<p>Found ${result.length} results for "${query}"</p>`)
    result.forEach(function (result) {
      searchData.then(function (data) {
        const item = data[result.ref]
        resultsText.append(`<p><a href="${item.url}">${item.display_string}</a></p>`)
      })
    })
    results.show()
  })
})
