%include	/usr/lib/rpm/macros.perl
Summary:	Math::SigFigs - do math with correct handling of significant figures
Summary(pl):	Math::SigFigs - obliczenia z poprawn± obs³ug± cyfr znacz±cych
Name:		perl-Math-SigFigs
Version:	1.01
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/Math/SigFigs-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
In many scientific applications, it is often useful to be able to
format numbers with a given number of significant figures, or to do
math in such a way as to maintain the correct number of significant
figures. The rules for significant figures are too complicated to be
handled solely using the sprintf function (unless you happen to be
Randal Schwartz :-).

%description -l pl
W wielu aplikacjach naukowych przydaje siê formatowanie liczb z zadan±
liczb± cyfr znacz±cych albo wykonywanie obliczeñ z zachowaniem
poprawnej liczby cyfr znacz±cych. Zasady dla cyfr znacz±cych s± zbyt
skomplikowane, by mog³y byæ obs³u¿one przez funkcjê sprint (chyba ¿e
kto¶ jest Randalem Schwartzem :-)).

%prep
%setup -q -n SigFigs-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%{perl_sitelib}/Math/SigFigs.pm
%{_mandir}/man3/*
