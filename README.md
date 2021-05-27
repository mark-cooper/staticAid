# StaticAid

A [Jekyll](http://jekyllrb.com/) static site generator for archival description serialized in JSON, generated via the
[ArchivesSpace](http://archivesspace.org) REST API, or by other modular backends which can be added to the system.

## Quick Start

Install [git](https://git-scm.com/) and clone the repository.

    $ git clone git@github.com:helrond/staticAid.git

Install [Docker](https://store.docker.com/search?type=edition&offering=community) and build the image using `docker-compose`.

    $ cd staticAid
    $ docker-compose build -t staticaid .

Start the container.

    $ docker-compose up

The site will build, and the staticAid interface built using sample data will then be available at http://localhost:4000 in your browser. Any changes to the templates in the `site/` directory or the python files in the `static_aid/` directory will result in a rebuild of the site or a reinstallation of the staticAid scripts, respectively.


## Usage

### Scripts

staticAid comes with bash scripts which will build the site in three different ways. In the Docker container in this repository, those scripts are installed in /usr/local/bin. If staticAid is deployed differently, you will need to find a way to make these scripts executable on the system.

You have three options for building the HTML site using Jekyll. In all cases, Jekyll will place the generated site in `build/site/`.

#### Build without updating data

Running `static-aid-build` will build the site based on the data currently in the
`build/data` directory.

#### Update data then build site

Running `static-aid-update` will fetch JSON for resource records, resource record
trees and archival objects from ArchivesSpace using `static_aid/get_json.py` and
save it in your `build/data` directory, then will build the site based on that data.

**WARNING**: Depending on the amount of data in of your ArchivesSpace instance,
it could take quite a while for this script to loop through all resource records
and components. Be patient!

#### Clean Build

Running `static-aid-rebuild` will wipe out the existing data, fetch new data, and
build the site from scratch.

**WARNING**: Depending on the amount of data in of your ArchivesSpace instance,
it could take quite a while for this script to loop through all resource records
and components. Be patient!

### JSON-LD Structured Data

By default, StaticAid is set up to generate structured data in your HTML in the
form of JSON-LD objects, coded according to the conventions of schema.org. JSON-LD
is Google's recommended method of delivering structured data for its indexing algorithms.
(More information [here](https://developers.google.com/search/docs/guides/intro-structured-data).)

Currently, JSON-LD objects are formed on three kinds of pages:

*   Main index page, describing the holding archive ([Schema](https://gist.github.com/scottythered/68750a6032d3e72fe0bcb83789b64b55))
*   Collection pages ([Schema](https://gist.github.com/scottythered/d79b8d63ca3a2da120f7efa3168ea8ac))
*   Persona and Corporate Agent detail pages ([Schemas](https://gist.github.com/scottythered/090b3d05495ae991d7779bf06d08781a))

Variables used in the JSON-LD objects (as well as a few others in building your site)
are stored in `local_settings.cfg`. If you don't want JSON-LD generated, you can
leave those variables undefined. The JSON-LD will be broken, but it will not affect
the display of the web pages.

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
Erin O'Meara / @diplomaticaerin  
Scott Carlson / @scottythered  

## License

staticAid is released under the MIT License. See `LICENSE.md` for more information.
