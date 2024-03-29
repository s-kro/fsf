Name:           fsf
Version:        0.1

Release:        2%{?dist}
Summary:        Free Software Federation Current Address

License:        MIT       
URL:            http://www.krotek.com

#Source0:        https://github.com/s-kro/fsf/blob/master/fsf.tar.xz
Source0:        https://github.com/s-kro/%{name}/archive/refs/tags/%{name}-%{version}-2.tar.gz

#Packager:       pappy

BuildRequires:  coreutils
BuildRequires:  perl-generators
BuildRequires:  perl-Module-Build
BuildRequires:  perl-Archive-Tar

Requires:       perl-File-Find-Rule

BuildArch:      noarch


%description
Updates the Free Software Federation's address to the latest.

%prep
%setup -q -n %{name}-%{version}-2
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
* Tue Mar 14 2023 Pappy Packager <skrochen@krotek.com> 0.2-1
- tag 0.1-2 

* Mon Mar 13 2023 Pappy Packager <skrochen@krotek.com>
- Repackage with tito

* Mon Mar 13 2023 pappy <skrochen@krotek.com> - 0.1-2
- Repackaging v0.1

* Mon Mar 13 2023 pappy <skrochen@krotek.com>
- new package built with tito

* Mon Mar 13 2023 pappy <skrochen@krotek.com> - 0.1-1
- Initial packaging v0.1

