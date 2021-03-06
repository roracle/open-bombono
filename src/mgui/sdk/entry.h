//
// mgui/sdk/entry.h
// This file is part of Bombono DVD project.
//
// Copyright (c) 2008 Ilya Murav'jov
//
// This program is free software; you can redistribute it and/or modify
// it under the terms of the GNU General Public License as published by
// the Free Software Foundation; either version 2 of the License, or
// (at your option) any later version.
//
// This program is distributed in the hope that it will be useful,
// but WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
// GNU General Public License for more details.
//
// You should have received a copy of the GNU General Public License
// along with this program; if not, write to the Free Software
// Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA
// 

#ifndef __MGUI_SDK_ENTRY_H__
#define __MGUI_SDK_ENTRY_H__

#include "gnc-gtk-utils.h"

//
// LimitTextInput - ограничение на ввод для Gtk::Entry
//

extern const char DigitChars[];
void LimitTextInput(Gtk::Entry& ent, const char* allowed_chars);

#endif // __MGUI_SDK_ENTRY_H__

