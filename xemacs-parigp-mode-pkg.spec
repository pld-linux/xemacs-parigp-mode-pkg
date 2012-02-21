Summary:	PARI/GP mode for XEmacs
Summary(pl.UTF-8):	Tryb edycji plików PARI/GP do XEmacsa
Name:		xemacs-parigp-mode-pkg
Version:	3.03
Release:	1
License:	GPL
Group:		Applications/Editors/Emacs
Source0:	http://math.univ-lille1.fr/~ramare/ServeurPerso/GP-PARI/latest-pari-distrib/pariemacs-%{version}.tar.gz
# Source0-md5:	d538ec9863e78070c460b55504a3f613
URL:		http://math.univ-lille1.fr/~ramare/ServeurPerso/GP-PARI/
BuildRequires:	pari >= 2.4.0
Requires:	xemacs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PARI/GP editing mode for Xemacs.

%description -l pl.UTF-8
Tryb edycji plików PARI/GP do Xemacsa.

%prep
%setup -q -n pariemacs-%{version}

%build
%{__make} pari-conf.el \
	INSTALL=%{_datadir}/xemacs-packages/lisp/parigp-mode \
	PARI_CFG=%{_libdir}/parigp/pari.cfg

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/parigp-mode
cp -a *.el $RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/parigp-mode
cat <<EOF >$RPM_BUILD_ROOT%{_datadir}/xemacs-packages/lisp/parigp-mode/auto-autoloads.el
(autoload 'gp-mode "pari" nil t)
(autoload 'gp-script-mode "pari" nil t)
(autoload 'gp "pari" nil t)
(autoload 'gpman "pari" nil t)
EOF

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{_datadir}/xemacs-packages/lisp/parigp-mode
