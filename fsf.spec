Name:           fsf
Version:        0.1

Release:        1%{?dist}
Summary:        Free Software Federation Current Address

License:        MIT       
URL:            http://www.krotek.com

Source0:        https://github.com/s-kro/fsf/blob/master/fsf.tar.xz

#Packager:       pappy
BuildRequires:  perl-generators
BuildRequires:  coreutils
#BuildRequires:  git

Requires:       perl-File-Find-Rule

BuildArch:      noarch


%description
Updates the Free Software Federation's address to the latest.

%prep
%setup -q -n %{name}
rm fsf.spec

%build

ls
perl Build.PL installdirs=vendor 'optimize=-O2 -g'
./Build
./Build manifest
./Build dist
##%{make_build}

%install
#./Build install
#%%{_fixperms} %%{buildroot}/*

#%%find_lang %%{name}

%files
#%%{perl_vendorlib}/*

#%%license COPYING
%doc README.md

%changelog

* Mon Mar 13 2023 pappy <skrochen@krotek.com> - 0.1-1
- Initial packaging v0.1

