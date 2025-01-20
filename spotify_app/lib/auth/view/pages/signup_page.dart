import 'package:flutter/material.dart';
import 'package:spotify_app/auth/view/widgets/auth_gradient_button.dart';
import 'package:spotify_app/auth/view/widgets/custom_field.dart';

import '../../../core/theme/app_pallete.dart';

class SignupPage extends StatefulWidget {
  const SignupPage({super.key});

  @override
  State<SignupPage> createState() => _SignupPageState();
}

class _SignupPageState extends State<SignupPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: Padding(
        padding: const EdgeInsets.all(15.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Sign Up.',
              style: TextStyle(fontSize: 50, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 30),
            const CustomField(
              HintText: 'Name',
            ),
            const SizedBox(height: 15),
            const CustomField(
              HintText: 'Email',
            ),
            const SizedBox(height: 15),
            const CustomField(
              HintText: 'Password',
            ),
            const SizedBox(
              height: 20,
            ),
            const AuthGradientButton(buttonText: 'Sign Up'),
            const SizedBox(
              height: 20,
            ),
            RichText(
              text: TextSpan(
                text: 'Already have an account? ',
                style: Theme.of(context).textTheme.titleMedium,
                children: const [
                  TextSpan(
                    text: 'Sign In.',
                    style: TextStyle(
                      color: Pallete.gradient2,
                      fontWeight: FontWeight.bold,
                    )
                  ),
                ],
              ),  
            ),
          ],
        ),
      ),
    );
  }
}
