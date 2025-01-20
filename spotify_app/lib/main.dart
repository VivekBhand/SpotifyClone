import 'package:flutter/material.dart';
import 'package:spotify_app/auth/view/pages/signup_page.dart';
import 'package:spotify_app/core/theme/theme.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Spotify Clone',
      theme: AppTheme.darkThemeMode,
      debugShowCheckedModeBanner: false,
      home: const SignupPage(),
    );
  }
}


