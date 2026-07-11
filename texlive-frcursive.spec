%global tl_name frcursive
%global tl_revision 77682

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	French cursive hand fonts
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/frcursive
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frcursive.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/frcursive.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A hand-writing font in the style of the French academic running-hand.
The font was written in Metafont and has been converted to Adobe Type 1
format. LaTeX support (NFSS fd files, and a package) and font maps are
provided.

