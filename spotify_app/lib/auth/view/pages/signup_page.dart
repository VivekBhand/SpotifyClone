import 'package:flutter/material.dart';
import 'package:spotify_app/auth/view/widgets/custom_field.dart';

class SignupPage extends StatefulWidget {
  const SignupPage({super.key});

  @override
  State<SignupPage> createState() => _SignupPageState();

}

class _SignupPageState extends State<SignupPage>{
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: const Padding(
        padding: EdgeInsets.all(15.0),
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              'Sign Up.',
              style: TextStyle(
                fontSize: 50,
                fontWeight: FontWeight.bold
              ),
            ),
            SizedBox(height : 30),
            CustomField(
              HintText: 'Name',
            ),
            SizedBox(height : 15),
            CustomField(
              HintText: 'Email',
            ),
            SizedBox(height : 15),
            CustomField(
              HintText: 'Password',
            ),

          ],
        ),
      ),
    );
  }
  
}