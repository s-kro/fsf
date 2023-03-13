use strict;
use warnings;
use Module::Build;

use 5.008;

my $builder = Module::Build->new(
    module_name         => 'fsf',
    license             => 'perl',
    dist_author         => 'SK <skrochen@krotek.com>',
    dist_abstract       => 'Script to update FSF address',
    create_makefile_pl  => 0,     #'traditional',
    script_files        => 'scripts/fsf.pl',
    create_readme       => 0,
    requires            => {
	'File::Find::Rule'      => '0',
    },
    build_requires      => {
	'Module::Build'       => '0.42',
	'Test::More'          => '0.47',
    },
    meta_merge => {
	resources => {
	    repository => 'https://github.com/s-kro/fsf',
	    bugtracker => 'https://github.com/s-kro/fsf/issues'
	}
    },
    );

$builder->create_build_script();
