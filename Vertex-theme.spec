#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Vertex-theme
Version  : 20150923
Release  : 9
URL      : https://github.com/horst3180/Vertex-theme/archive/20150923.tar.gz
Source0  : https://github.com/horst3180/Vertex-theme/archive/20150923.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-2.1
Requires: Vertex-theme-data

%description
*************
* Important *
*************
This file fixes the issues of Ubuntu-Software-Center with the Vertex-Dark theme. Only install this if you are using Vertex-Dark

%package data
Summary: data components for the Vertex-theme package.
Group: Data

%description data
data components for the Vertex-theme package.


%prep
%setup -q -n Vertex-theme-20150923

%build
%autogen --disable-static --disable-cinnamon --disable-gnome-shell --disable-gtk3 --disable-metacity --disable-unity --enable-xfwm
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-down-insens.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-down-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-down-small-insens.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-down-small-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-down-small.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-down.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-left-insens.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-left-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-left.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-right-insens.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-right-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-right.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-up-insens.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-up-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-up-small-insens.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-up-small-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-up-small.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/arrow-up.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/menu-arrow-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Arrows/menu-arrow.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Buttons/button-default-nohilight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Buttons/button-default.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Buttons/button-default.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Buttons/button-insensitive-nohilight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Buttons/button-insensitive.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Buttons/button-prelight-nohilight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Buttons/button-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Buttons/button-pressed-nohilight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Buttons/button-pressed.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/checkbox-checked-insensitive.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/checkbox-checked.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/checkbox-unchecked-insensitive.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/checkbox-unchecked.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-checkbox-checked-hover.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-checkbox-checked-hover.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-checkbox-checked-insensitive.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-checkbox-checked-insensitive.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-checkbox-checked.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-checkbox-checked.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-checkbox-unchecked-insensitive.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-checkbox-unchecked-insensitive.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-checkbox-unchecked.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-checkbox-unchecked.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-option-checked-hover.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-option-checked-hover.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-option-checked-insensitive.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-option-checked-insensitive.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-option-checked.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-option-checked.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-option-unchecked-insensitive.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-option-unchecked-insensitive.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-option-unchecked.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/menu-option-unchecked.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/option-checked-insensitive.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/option-checked.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/option-unchecked-insensitive.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Check-Radio/option-unchecked.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-active-bg.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-active-notebook.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-active-rtl-bg.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-active-rtl-notebook.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-bg.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-disabled-bg.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-disabled-notebook.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-disabled-rtl-bg.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-disabled-rtl-notebook.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-notebook.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-rtl-bg.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-border-rtl-notebook.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-button-active-rtl.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-button-active.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-button-disabled-rtl.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-button-disabled.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-button-rtl.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/combo-entry-button.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-active-bg-solid.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-active-bg.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-active-notebook.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-bg-solid.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-bg.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-disabled-bg.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-disabled-notebook.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-fill-plain.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-fill-solid.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-fill.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/entry-border-notebook.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/ff-entry-bg.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Entry/ff-entry.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Expanders/minus.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Expanders/plus.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Handles/handle-h.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Handles/handle-v.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Lines/line-h.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Lines/line-v.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Lines/menu_line_h.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Menu-Menubar/menubar_button.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Menu/menuitem.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Others/focus.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Others/null.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Others/tree_header.png
/usr/share/themes/Vertex-Dark/gtk-2.0/ProgressBar/progressbar.png
/usr/share/themes/Vertex-Dark/gtk-2.0/ProgressBar/progressbar_v.png
/usr/share/themes/Vertex-Dark/gtk-2.0/ProgressBar/trough-progressbar.png
/usr/share/themes/Vertex-Dark/gtk-2.0/ProgressBar/trough-progressbar_v.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Range/slider-horiz-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Range/slider-horiz.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Range/slider-vert-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Range/slider-vert.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Range/trough-horizontal.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Range/trough-vertical.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Scrollbars/slider-horiz-active.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Scrollbars/slider-horiz-insens.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Scrollbars/slider-horiz-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Scrollbars/slider-horiz.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Scrollbars/slider-vert-active.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Scrollbars/slider-vert-insens.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Scrollbars/slider-vert-prelight.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Scrollbars/slider-vert.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Scrollbars/trough-scrollbar-horiz.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Scrollbars/trough-scrollbar-vert.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Shadows/frame-gap-end.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Shadows/frame-gap-start.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Shadows/frame.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Spin/down-background-disable-rtl.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Spin/down-background-disable.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Spin/down-background-rtl.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Spin/down-background.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Spin/up-background-disable-rtl.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Spin/up-background-disable.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Spin/up-background-rtl.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Spin/up-background.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/notebook-gap-horiz.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/notebook-gap-vert.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/notebook.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/tab-bottom-active.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/tab-bottom.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/tab-left-active.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/tab-left.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/tab-right-active.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/tab-right.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/tab-top-active.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/tab-top.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Tabs/tab.svg
/usr/share/themes/Vertex-Dark/gtk-2.0/Toolbar/inline-toolbar.png
/usr/share/themes/Vertex-Dark/gtk-2.0/Toolbar/toolbar.png
/usr/share/themes/Vertex-Dark/gtk-2.0/gtkrc
/usr/share/themes/Vertex-Dark/gtk-2.0/panel.rc
/usr/share/themes/Vertex-Dark/index.theme
/usr/share/themes/Vertex-Dark/xfwm4/bottom-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/bottom-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/bottom-left-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/bottom-left-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/bottom-right-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/bottom-right-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/close-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/close-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/close-prelight.xpm
/usr/share/themes/Vertex-Dark/xfwm4/close-pressed.xpm
/usr/share/themes/Vertex-Dark/xfwm4/hide-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/hide-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/hide-prelight.xpm
/usr/share/themes/Vertex-Dark/xfwm4/hide-pressed.xpm
/usr/share/themes/Vertex-Dark/xfwm4/left-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/left-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/maximize-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/maximize-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/maximize-prelight.xpm
/usr/share/themes/Vertex-Dark/xfwm4/maximize-pressed.xpm
/usr/share/themes/Vertex-Dark/xfwm4/menu-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/menu-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/menu-pressed.xpm
/usr/share/themes/Vertex-Dark/xfwm4/right-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/right-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/shade-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/shade-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/shade-pressed.xpm
/usr/share/themes/Vertex-Dark/xfwm4/stick-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/stick-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/stick-pressed.xpm
/usr/share/themes/Vertex-Dark/xfwm4/themerc
/usr/share/themes/Vertex-Dark/xfwm4/title-1-active-shaded.xpm
/usr/share/themes/Vertex-Dark/xfwm4/title-1-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/title-1-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/title-2-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/title-2-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/title-3-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/title-3-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/title-4-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/title-4-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/title-5-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/title-5-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/top-left-active-shaded.xpm
/usr/share/themes/Vertex-Dark/xfwm4/top-left-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/top-left-inactive.xpm
/usr/share/themes/Vertex-Dark/xfwm4/top-right-active-shaded.xpm
/usr/share/themes/Vertex-Dark/xfwm4/top-right-active.xpm
/usr/share/themes/Vertex-Dark/xfwm4/top-right-inactive.xpm
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-down-insens.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-down-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-down-small-insens.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-down-small-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-down-small.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-down.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-left-insens.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-left-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-left.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-right-insens.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-right-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-right.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-up-insens.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-up-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-up-small-insens.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-up-small-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-up-small.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/arrow-up.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/menu-arrow-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Arrows/menu-arrow.png
/usr/share/themes/Vertex-Light/gtk-2.0/Buttons/button-default-nohilight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Buttons/button-default.png
/usr/share/themes/Vertex-Light/gtk-2.0/Buttons/button-default.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Buttons/button-insensitive-nohilight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Buttons/button-insensitive.png
/usr/share/themes/Vertex-Light/gtk-2.0/Buttons/button-prelight-nohilight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Buttons/button-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Buttons/button-pressed-alt.png
/usr/share/themes/Vertex-Light/gtk-2.0/Buttons/button-pressed-nohilight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Buttons/button-pressed.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/checkbox-checked-insensitive.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/checkbox-checked.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/checkbox-unchecked-insensitive.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/checkbox-unchecked.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-checkbox-checked-hover.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-checkbox-checked-hover.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-checkbox-checked-insensitive.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-checkbox-checked-insensitive.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-checkbox-checked.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-checkbox-checked.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-checkbox-unchecked-insensitive.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-checkbox-unchecked-insensitive.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-checkbox-unchecked.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-checkbox-unchecked.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-option-checked-hover.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-option-checked-hover.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-option-checked-insensitive.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-option-checked-insensitive.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-option-checked.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-option-checked.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-option-unchecked-insensitive.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-option-unchecked-insensitive.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-option-unchecked.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/menu-option-unchecked.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/option-checked-insensitive.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/option-checked.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/option-unchecked-insensitive.png
/usr/share/themes/Vertex-Light/gtk-2.0/Check-Radio/option-unchecked.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-active-bg.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-active-notebook.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-active-rtl-bg.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-active-rtl-notebook.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-bg.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-disabled-bg.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-disabled-notebook.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-disabled-rtl-bg.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-disabled-rtl-notebook.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-notebook.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-rtl-bg.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-border-rtl-notebook.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-button-active-rtl.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-button-active.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-button-disabled-rtl.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-button-disabled.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-button-rtl.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/combo-entry-button.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-active-bg-solid.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-active-bg.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-active-notebook.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-bg-solid.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-bg.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-disabled-bg.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-disabled-notebook.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-fill-plain.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-fill-solid.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-fill.png
/usr/share/themes/Vertex-Light/gtk-2.0/Entry/entry-border-notebook.png
/usr/share/themes/Vertex-Light/gtk-2.0/Expanders/minus.png
/usr/share/themes/Vertex-Light/gtk-2.0/Expanders/plus.png
/usr/share/themes/Vertex-Light/gtk-2.0/Handles/handle-h.png
/usr/share/themes/Vertex-Light/gtk-2.0/Handles/handle-v.png
/usr/share/themes/Vertex-Light/gtk-2.0/Lines/line-h.png
/usr/share/themes/Vertex-Light/gtk-2.0/Lines/line-v.png
/usr/share/themes/Vertex-Light/gtk-2.0/Lines/menu_line_h.png
/usr/share/themes/Vertex-Light/gtk-2.0/Menu-Menubar/menubar_button.png
/usr/share/themes/Vertex-Light/gtk-2.0/Menu/menuitem.png
/usr/share/themes/Vertex-Light/gtk-2.0/Others/focus.png
/usr/share/themes/Vertex-Light/gtk-2.0/Others/null.png
/usr/share/themes/Vertex-Light/gtk-2.0/Others/tree_header.png
/usr/share/themes/Vertex-Light/gtk-2.0/ProgressBar/progressbar.png
/usr/share/themes/Vertex-Light/gtk-2.0/ProgressBar/progressbar_v.png
/usr/share/themes/Vertex-Light/gtk-2.0/ProgressBar/trough-progressbar.png
/usr/share/themes/Vertex-Light/gtk-2.0/ProgressBar/trough-progressbar_v.png
/usr/share/themes/Vertex-Light/gtk-2.0/Range/slider-horiz-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Range/slider-horiz.png
/usr/share/themes/Vertex-Light/gtk-2.0/Range/slider-vert-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Range/slider-vert.png
/usr/share/themes/Vertex-Light/gtk-2.0/Range/trough-horizontal.png
/usr/share/themes/Vertex-Light/gtk-2.0/Range/trough-vertical.png
/usr/share/themes/Vertex-Light/gtk-2.0/Scrollbars/slider-horiz-active.png
/usr/share/themes/Vertex-Light/gtk-2.0/Scrollbars/slider-horiz-insens.png
/usr/share/themes/Vertex-Light/gtk-2.0/Scrollbars/slider-horiz-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Scrollbars/slider-horiz.png
/usr/share/themes/Vertex-Light/gtk-2.0/Scrollbars/slider-vert-active.png
/usr/share/themes/Vertex-Light/gtk-2.0/Scrollbars/slider-vert-insens.png
/usr/share/themes/Vertex-Light/gtk-2.0/Scrollbars/slider-vert-prelight.png
/usr/share/themes/Vertex-Light/gtk-2.0/Scrollbars/slider-vert.png
/usr/share/themes/Vertex-Light/gtk-2.0/Scrollbars/trough-scrollbar-horiz.png
/usr/share/themes/Vertex-Light/gtk-2.0/Scrollbars/trough-scrollbar-vert.png
/usr/share/themes/Vertex-Light/gtk-2.0/Shadows/frame-gap-end.png
/usr/share/themes/Vertex-Light/gtk-2.0/Shadows/frame-gap-start.png
/usr/share/themes/Vertex-Light/gtk-2.0/Shadows/frame.png
/usr/share/themes/Vertex-Light/gtk-2.0/Spin/down-background-disable-rtl.png
/usr/share/themes/Vertex-Light/gtk-2.0/Spin/down-background-disable.png
/usr/share/themes/Vertex-Light/gtk-2.0/Spin/down-background-rtl.png
/usr/share/themes/Vertex-Light/gtk-2.0/Spin/down-background.png
/usr/share/themes/Vertex-Light/gtk-2.0/Spin/up-background-disable-rtl.png
/usr/share/themes/Vertex-Light/gtk-2.0/Spin/up-background-disable.png
/usr/share/themes/Vertex-Light/gtk-2.0/Spin/up-background-rtl.png
/usr/share/themes/Vertex-Light/gtk-2.0/Spin/up-background.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/notebook-gap-horiz.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/notebook-gap-vert.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/notebook.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/tab-bottom-active.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/tab-bottom.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/tab-left-active.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/tab-left.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/tab-right-active.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/tab-right.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/tab-top-active.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/tab-top.png
/usr/share/themes/Vertex-Light/gtk-2.0/Tabs/tab.svg
/usr/share/themes/Vertex-Light/gtk-2.0/Toolbar/inline-toolbar.png
/usr/share/themes/Vertex-Light/gtk-2.0/Toolbar/toolbar.png
/usr/share/themes/Vertex-Light/gtk-2.0/gtkrc
/usr/share/themes/Vertex-Light/gtk-2.0/panel.rc
/usr/share/themes/Vertex-Light/index.theme
/usr/share/themes/Vertex-Light/xfwm4/bottom-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/bottom-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/bottom-left-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/bottom-left-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/bottom-right-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/bottom-right-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/close-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/close-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/close-prelight.xpm
/usr/share/themes/Vertex-Light/xfwm4/close-pressed.xpm
/usr/share/themes/Vertex-Light/xfwm4/hide-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/hide-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/hide-prelight.xpm
/usr/share/themes/Vertex-Light/xfwm4/hide-pressed.xpm
/usr/share/themes/Vertex-Light/xfwm4/left-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/left-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/maximize-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/maximize-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/maximize-prelight.xpm
/usr/share/themes/Vertex-Light/xfwm4/maximize-pressed.xpm
/usr/share/themes/Vertex-Light/xfwm4/menu-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/menu-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/menu-pressed.xpm
/usr/share/themes/Vertex-Light/xfwm4/right-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/right-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/shade-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/shade-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/shade-pressed.xpm
/usr/share/themes/Vertex-Light/xfwm4/stick-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/stick-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/stick-pressed.xpm
/usr/share/themes/Vertex-Light/xfwm4/themerc
/usr/share/themes/Vertex-Light/xfwm4/title-1-active-shaded.xpm
/usr/share/themes/Vertex-Light/xfwm4/title-1-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/title-1-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/title-2-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/title-2-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/title-3-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/title-3-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/title-4-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/title-4-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/title-5-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/title-5-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/top-left-active-shaded.xpm
/usr/share/themes/Vertex-Light/xfwm4/top-left-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/top-left-inactive.xpm
/usr/share/themes/Vertex-Light/xfwm4/top-right-active-shaded.xpm
/usr/share/themes/Vertex-Light/xfwm4/top-right-active.xpm
/usr/share/themes/Vertex-Light/xfwm4/top-right-inactive.xpm
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-down-insens.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-down-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-down-small-insens.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-down-small-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-down-small.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-down.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-left-insens.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-left-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-left.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-right-insens.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-right-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-right.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-up-insens.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-up-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-up-small-insens.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-up-small-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-up-small.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/arrow-up.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/menu-arrow-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Arrows/menu-arrow.png
/usr/share/themes/Vertex/gtk-2.0/Buttons/button-default-nohilight.png
/usr/share/themes/Vertex/gtk-2.0/Buttons/button-default.png
/usr/share/themes/Vertex/gtk-2.0/Buttons/button-default.svg
/usr/share/themes/Vertex/gtk-2.0/Buttons/button-insensitive-nohilight.png
/usr/share/themes/Vertex/gtk-2.0/Buttons/button-insensitive.png
/usr/share/themes/Vertex/gtk-2.0/Buttons/button-prelight-nohilight.png
/usr/share/themes/Vertex/gtk-2.0/Buttons/button-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Buttons/button-pressed-alt.png
/usr/share/themes/Vertex/gtk-2.0/Buttons/button-pressed-nohilight.png
/usr/share/themes/Vertex/gtk-2.0/Buttons/button-pressed.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/checkbox-checked-insensitive.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/checkbox-checked.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/checkbox-unchecked-insensitive.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/checkbox-unchecked.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-checkbox-checked-hover.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-checkbox-checked-hover.svg
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-checkbox-checked-insensitive.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-checkbox-checked-insensitive.svg
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-checkbox-checked.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-checkbox-checked.svg
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-checkbox-unchecked-insensitive.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-checkbox-unchecked-insensitive.svg
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-checkbox-unchecked.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-checkbox-unchecked.svg
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-option-checked-hover.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-option-checked-hover.svg
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-option-checked-insensitive.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-option-checked-insensitive.svg
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-option-checked.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-option-checked.svg
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-option-unchecked-insensitive.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-option-unchecked-insensitive.svg
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-option-unchecked.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/menu-option-unchecked.svg
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/option-checked-insensitive.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/option-checked.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/option-unchecked-insensitive.png
/usr/share/themes/Vertex/gtk-2.0/Check-Radio/option-unchecked.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-active-bg.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-active-notebook.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-active-rtl-bg.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-active-rtl-notebook.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-bg.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-disabled-bg.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-disabled-notebook.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-disabled-rtl-bg.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-disabled-rtl-notebook.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-notebook.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-rtl-bg.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-border-rtl-notebook.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-button-active-rtl.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-button-active.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-button-disabled-rtl.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-button-disabled.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-button-rtl.png
/usr/share/themes/Vertex/gtk-2.0/Entry/combo-entry-button.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-active-bg-solid.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-active-bg.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-active-notebook.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-bg-solid.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-bg.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-disabled-bg.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-disabled-notebook.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-fill-plain.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-fill-solid.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-fill.png
/usr/share/themes/Vertex/gtk-2.0/Entry/entry-border-notebook.png
/usr/share/themes/Vertex/gtk-2.0/Expanders/minus.png
/usr/share/themes/Vertex/gtk-2.0/Expanders/plus.png
/usr/share/themes/Vertex/gtk-2.0/Handles/handle-h.png
/usr/share/themes/Vertex/gtk-2.0/Handles/handle-v.png
/usr/share/themes/Vertex/gtk-2.0/Lines/line-h.png
/usr/share/themes/Vertex/gtk-2.0/Lines/line-v.png
/usr/share/themes/Vertex/gtk-2.0/Lines/menu_line_h.png
/usr/share/themes/Vertex/gtk-2.0/Menu-Menubar/menubar_button.png
/usr/share/themes/Vertex/gtk-2.0/Menu/menuitem.png
/usr/share/themes/Vertex/gtk-2.0/Others/focus.png
/usr/share/themes/Vertex/gtk-2.0/Others/null.png
/usr/share/themes/Vertex/gtk-2.0/Others/tree_header.png
/usr/share/themes/Vertex/gtk-2.0/ProgressBar/progressbar.png
/usr/share/themes/Vertex/gtk-2.0/ProgressBar/progressbar_v.png
/usr/share/themes/Vertex/gtk-2.0/ProgressBar/trough-progressbar.png
/usr/share/themes/Vertex/gtk-2.0/ProgressBar/trough-progressbar_v.png
/usr/share/themes/Vertex/gtk-2.0/Range/slider-horiz-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Range/slider-horiz.png
/usr/share/themes/Vertex/gtk-2.0/Range/slider-vert-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Range/slider-vert.png
/usr/share/themes/Vertex/gtk-2.0/Range/trough-horizontal.png
/usr/share/themes/Vertex/gtk-2.0/Range/trough-vertical.png
/usr/share/themes/Vertex/gtk-2.0/Scrollbars/slider-horiz-active.png
/usr/share/themes/Vertex/gtk-2.0/Scrollbars/slider-horiz-insens.png
/usr/share/themes/Vertex/gtk-2.0/Scrollbars/slider-horiz-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Scrollbars/slider-horiz.png
/usr/share/themes/Vertex/gtk-2.0/Scrollbars/slider-vert-active.png
/usr/share/themes/Vertex/gtk-2.0/Scrollbars/slider-vert-insens.png
/usr/share/themes/Vertex/gtk-2.0/Scrollbars/slider-vert-prelight.png
/usr/share/themes/Vertex/gtk-2.0/Scrollbars/slider-vert.png
/usr/share/themes/Vertex/gtk-2.0/Scrollbars/trough-scrollbar-horiz.png
/usr/share/themes/Vertex/gtk-2.0/Scrollbars/trough-scrollbar-vert.png
/usr/share/themes/Vertex/gtk-2.0/Shadows/frame-gap-end.png
/usr/share/themes/Vertex/gtk-2.0/Shadows/frame-gap-start.png
/usr/share/themes/Vertex/gtk-2.0/Shadows/frame.png
/usr/share/themes/Vertex/gtk-2.0/Spin/down-background-disable-rtl.png
/usr/share/themes/Vertex/gtk-2.0/Spin/down-background-disable.png
/usr/share/themes/Vertex/gtk-2.0/Spin/down-background-rtl.png
/usr/share/themes/Vertex/gtk-2.0/Spin/down-background.png
/usr/share/themes/Vertex/gtk-2.0/Spin/up-background-disable-rtl.png
/usr/share/themes/Vertex/gtk-2.0/Spin/up-background-disable.png
/usr/share/themes/Vertex/gtk-2.0/Spin/up-background-rtl.png
/usr/share/themes/Vertex/gtk-2.0/Spin/up-background.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/notebook-gap-horiz.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/notebook-gap-vert.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/notebook.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/tab-bottom-active.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/tab-bottom.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/tab-left-active.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/tab-left.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/tab-right-active.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/tab-right.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/tab-top-active.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/tab-top.png
/usr/share/themes/Vertex/gtk-2.0/Tabs/tab.svg
/usr/share/themes/Vertex/gtk-2.0/Toolbar/inline-toolbar.png
/usr/share/themes/Vertex/gtk-2.0/Toolbar/toolbar.png
/usr/share/themes/Vertex/gtk-2.0/gtkrc
/usr/share/themes/Vertex/gtk-2.0/panel.rc
/usr/share/themes/Vertex/index.theme
/usr/share/themes/Vertex/xfwm4/bottom-active.xpm
/usr/share/themes/Vertex/xfwm4/bottom-inactive.xpm
/usr/share/themes/Vertex/xfwm4/bottom-left-active.xpm
/usr/share/themes/Vertex/xfwm4/bottom-left-inactive.xpm
/usr/share/themes/Vertex/xfwm4/bottom-right-active.xpm
/usr/share/themes/Vertex/xfwm4/bottom-right-inactive.xpm
/usr/share/themes/Vertex/xfwm4/close-active.xpm
/usr/share/themes/Vertex/xfwm4/close-inactive.xpm
/usr/share/themes/Vertex/xfwm4/close-prelight.xpm
/usr/share/themes/Vertex/xfwm4/close-pressed.xpm
/usr/share/themes/Vertex/xfwm4/hide-active.xpm
/usr/share/themes/Vertex/xfwm4/hide-inactive.xpm
/usr/share/themes/Vertex/xfwm4/hide-prelight.xpm
/usr/share/themes/Vertex/xfwm4/hide-pressed.xpm
/usr/share/themes/Vertex/xfwm4/left-active.xpm
/usr/share/themes/Vertex/xfwm4/left-inactive.xpm
/usr/share/themes/Vertex/xfwm4/maximize-active.xpm
/usr/share/themes/Vertex/xfwm4/maximize-inactive.xpm
/usr/share/themes/Vertex/xfwm4/maximize-prelight.xpm
/usr/share/themes/Vertex/xfwm4/maximize-pressed.xpm
/usr/share/themes/Vertex/xfwm4/menu-active.xpm
/usr/share/themes/Vertex/xfwm4/menu-inactive.xpm
/usr/share/themes/Vertex/xfwm4/menu-pressed.xpm
/usr/share/themes/Vertex/xfwm4/right-active.xpm
/usr/share/themes/Vertex/xfwm4/right-inactive.xpm
/usr/share/themes/Vertex/xfwm4/shade-active.xpm
/usr/share/themes/Vertex/xfwm4/shade-inactive.xpm
/usr/share/themes/Vertex/xfwm4/shade-pressed.xpm
/usr/share/themes/Vertex/xfwm4/stick-active.xpm
/usr/share/themes/Vertex/xfwm4/stick-inactive.xpm
/usr/share/themes/Vertex/xfwm4/stick-pressed.xpm
/usr/share/themes/Vertex/xfwm4/themerc
/usr/share/themes/Vertex/xfwm4/title-1-active-shaded.xpm
/usr/share/themes/Vertex/xfwm4/title-1-active.xpm
/usr/share/themes/Vertex/xfwm4/title-1-inactive.xpm
/usr/share/themes/Vertex/xfwm4/title-2-active.xpm
/usr/share/themes/Vertex/xfwm4/title-2-inactive.xpm
/usr/share/themes/Vertex/xfwm4/title-3-active.xpm
/usr/share/themes/Vertex/xfwm4/title-3-inactive.xpm
/usr/share/themes/Vertex/xfwm4/title-4-active.xpm
/usr/share/themes/Vertex/xfwm4/title-4-inactive.xpm
/usr/share/themes/Vertex/xfwm4/title-5-active.xpm
/usr/share/themes/Vertex/xfwm4/title-5-inactive.xpm
/usr/share/themes/Vertex/xfwm4/top-left-active-shaded.xpm
/usr/share/themes/Vertex/xfwm4/top-left-active.xpm
/usr/share/themes/Vertex/xfwm4/top-left-inactive.xpm
/usr/share/themes/Vertex/xfwm4/top-right-active-shaded.xpm
/usr/share/themes/Vertex/xfwm4/top-right-active.xpm
/usr/share/themes/Vertex/xfwm4/top-right-inactive.xpm
