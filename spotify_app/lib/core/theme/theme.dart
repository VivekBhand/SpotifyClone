import 'package:flutter/material.dart';
import 'package:spotify_app/core/theme/app_pallete.dart';

class AppTheme {
  static final darkThemeMode = ThemeData.dark().copyWith(
      scaffoldBackgroundColor: Pallete.backgroundColor,
      appBarTheme: const AppBarTheme(backgroundColor: Pallete.backgroundColor),
      inputDecorationTheme: InputDecorationTheme(
        contentPadding: const EdgeInsets.all(27),
        enabledBorder: OutlineInputBorder(
          borderSide: const BorderSide(
            color: Pallete.borderColor,
            width: 3,
          ),
          borderRadius: BorderRadius.circular(10)
        ),
        focusedBorder: OutlineInputBorder(
            borderSide: const BorderSide(
              color: Pallete.gradient2,
              width: 3,
            ),
            borderRadius: BorderRadius.circular(10)
        ),
      ));
}
