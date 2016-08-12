# StaticAid

A [Jekyll](http://jekyllrb.com/) static site generator for archival description serialized in JSON, generated via the
[ArchivesSpace](http://archivesspace.org) REST API, or by other modular backends which can be added to the system.

You can see a live version of this site with sample data [here](http://hillelarnold.com/staticAid/).

## Requirements

*   [Python](https://wiki.python.org/moin/BeginnersGuide) (tested on v2.7)
*   Python Modules:

    *   [requests](http://www.python-requests.org/en/latest/)
    *   [requests_toolbelt](https://github.com/sigmavirus24/requests-toolbelt)
    *   [psutil](https://github.com/giampaolo/psutil)


*   [Jekyll](http://jekyllrb.com/) (to build the site)
*   [Node Package Manager or NPM](https://www.npmjs.com/)
*   [Grunt](http://gruntjs.com/getting-started) (for running build and deployment tasks)
*   An [ArchivesSpace](http://archivesspace.org/) or Adlib instance with some data entered (a sample data set is included for testing).

## Installation

### Setup

1.  Clone this repository `git clone git@github.com:helrond/staticAid.git` or download the ZIP file.
2.  Install dependencies. See "Requirements" above for a list of things you'll need to have installed.
3.  In this project's root directory, run `npm install` to install dependencies for Grunt.
4.  Review the default settings in `local_settings.default`; if you'd like to change them, copy this file
    to `local_settings.cfg` and make your changes. Otherwise, this file will be created for you.
5.  Change the values in `_config.yml` to match your preferences. Make sure to change `url` and `baseurl`.

**NOTE:** For Linux-like systems, you can simply run `install.sh`. 
It has only been tested on Mint 18+ and Ubuntu 16+, but should work on any Debian based distribution, 
OSX, RedHat, etc. with minimal modification.

## Usage

### Building the HTML Site

You have three options for building the HTML site using Jekyll. In all cases, Jekyll will place the generated site
in `build/site/`.

#### Build without updating data

Running `grunt build` will build the site based on the data currently in the `build/data` directory.

#### Update data then build site

Running `grunt update` will fetch JSON for resource records, resource record trees and archival objects from ArchivesSpace 
using `static_aid/getJson.py` and save it in your `build/data` directory, then will build the site based on that data.

**WARNING**: Depending on the size of your ArchivesSpace installation, it could take quite a while for this script to
loop through all resource records and components. Be patient!

#### Clean Build

By default, `grunt update` will only fetch JSON updated since the last time `static_aid/getJson.py` completed successfully. 
At any point, you can run `grunt rebuild` to wipe out the existing data and build the site from scratch.

**WARNING**: Depending on the size of your ArchivesSpace installation, it could take quite a while for this script to
loop through all resource records and components. Be patient!

### Starting the Local Server

To start a local server (useful for previewing the site), run `grunt serve`. You can then access the site by opening a
browser and pointing it to `http://localhost:4000`. To stop the server, use `ctrl + c`.

This server will use the HTML generated by the last build, so if you've made changes to any of your templates or data
you'll need to build the site in order to see those changes (see above).

### Github Pages

Github Pages support Jekyll sites, so a quick way to make your description publicly accessible is to push to a
`gh-pages` branch in a Github repository. See the [Github Pages](https://pages.github.com/) documentation
for more information.

### Auto Generating StaticAid Content via Cron Job

If you would like to auto-generate StaticAid content using a cron job (on OSX/Linux systems), you can
link one of the rebuild scripts to an appropriate cron job folder. To auto-generate full-page
content every day, you could do this:

    sudo ln -s scripts/static-aid-rebuild /etc/cron.daily/

or to auto-generate embedded content every week, you could do this:

    sudo ln -s scripts/static-aid-rebuild-embedded /etc/cron.weekly/

**NOTE:** it is important to softlink (`ln -s src dest`) instead of copying (`cp src dest`). 

## Contributing

Pull requests accepted! Feel free to file issues on this repository as well.

## Authors

Hillel Arnold / @helrond
Kevin Clair / @jackflaps
Luke Scott / @v-lukes
Erin O'Meara / @diplomatica


## License

staticAid is released under the MIT License. See `LICENSE.md` for more information.
