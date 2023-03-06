#! /usr/bin/perl

use strict;
use warnings;

use File::Find::Rule;


my $start = shift || '.';
print "fsf.pl searching $start ";

my $n = 0;
my @add_old;
push @add_old, '675 Mass Ave, Cambridge, MA 02139, USA';
push @add_old, '59 Temple Place, Suite 330, Boston, MA\s+02111(?:\-1307)?\s+USA';

my $add_old = join '|', @add_old;
my $add_new = '51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA';

for my $file (File::Find::Rule->in($start)) {
    next unless $file =~ /\.(?:c|cc|h|hh|scm|py|pl|inx|tcl|txt)$/;

    my $change = 0;
    my $last_change = 0;
    open C_FILE, "< $file" or die "Can't open file: $file $!";
    # print "Checking $file\n";

    my $f = do { local(@ARGV, $/) = $file; <>};

    if ($f =~ /$add_old/) {
	$f =~ s/$add_old/$add_new/;
	$n++;
	print "$n: FSF address updated in file: $file  ";
	$change = 1;
    }
    if ($f =~ /interpreter="python"/) {
	$f =~ s/interpreter="python"/interpreter="python2"/;
	$n++;
	print "$n: Python interpreter $file ";
	$change = 1;
    }

    if ($change) {
	open C_FILE, "> $file" or die "Can't open file: $file $!";
	print C_FILE $f;
    } 
    close C_FILE or die "Can't close file: $!";
    $last_change = $n;
}
