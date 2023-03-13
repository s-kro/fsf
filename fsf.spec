Name:           fsf
Version:        0.1

Release:        1%{?dist}
Summary:        FSF Current Address

License:        MIT       
URL:            http://www.krotek.com

Source0:        https://github.com/s-kro/fsf/blob/master/fsf.pl

#Packager:       pappy

BuildRequires:  coreutils
#BuildRequires:  git

Requires:       perl-File-Find-Rule

BuildArch:      noarch


%description
Updates FSF address to latest.


%build

%install
%{_fixperms} $RPM_BUILD_ROOT/*

#%%find_lang %%{name}

%files
%{perl_vendorlib}/*

#%%license COPYING
%doc README.md

%changelog

* Mon Mar 13 2023 pappy <skrochen@krotek.com> - 0.1-1
- Initial packaging v0.1

