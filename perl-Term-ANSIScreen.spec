#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define	pnam	ANSIScreen
Summary:	Term::ANSIScreen - terminal control using ANSI escape sequences
Summary(pl):	Term::ANSIScreen - sterowanie terminalem przy u¿yciu sekwencji ANSI
Name:		perl-Term-ANSIScreen
Version:	1.42
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	fae3a1c63e16905bf3d8a923d6f928b4
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Term::ANSIScreen is a superset of Term::ANSIColor (as of version 1.04
of that module). In addition to color-sequence generating subroutines
exported by :color and :constants, this module also features :cursor
for cursor positioning, :screen for screen control, as well as
:keyboard for key mapping.

%description -l pl
Term::ANSIScreen to nadzbiór Term::ANSIColor (przynajmniej dla wersji
1.04 tamtego modu³u). Oprócz funkcji generuj±cych sekwencje dla
kolorów ekportowanych przez :color i :constants, ten modu³ ma tak¿e
:cursor do ustawiania kursora, :screen do sterowania ekranem, a tak¿e
:keyboard do mapowania klawiszy.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Term/ANSIScreen.pm
%{_mandir}/man3/*
