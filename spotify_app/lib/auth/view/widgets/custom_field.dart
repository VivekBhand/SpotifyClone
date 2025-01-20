import 'package:flutter/material.dart';

class CustomField extends StatelessWidget {
  final String HintText;
  const CustomField({super.key, required this.HintText,});

  @override
  Widget build(BuildContext context) {
    return TextFormField(
      decoration: InputDecoration(
        hintText: HintText
      ),
    );
  }
}
