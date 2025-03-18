import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: PredictionPage(),
    );
  }
}

class PredictionPage extends StatefulWidget {
  @override
  _PredictionPageState createState() => _PredictionPageState();
}

class _PredictionPageState extends State<PredictionPage> {
  final _formKey = GlobalKey<FormState>();
  final Map<String, dynamic> _inputData = {};
  String _prediction = '';

  Future<void> _predict() async {
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save();
      final response = await http.post(
        Uri.parse('https://your-api-url.onrender.com/predict'),
        headers: {'Content-Type': 'application/json'},
        body: json.encode(_inputData),
      );
      if (response.statusCode == 200) {
        setState(() {
          _prediction = json.decode(response.body)['prediction'].toString();
        });
      } else {
        setState(() {
          _prediction = 'Error: ${response.statusCode}';
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text('Wine Quality Predictor')),
      body: Padding(
        padding: EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: ListView(
            children: [
              TextFormField(
                decoration: InputDecoration(labelText: 'Fixed Acidity'),
                keyboardType: TextInputType.number,
                onSaved: (value) => _inputData['fixed_acidity'] = double.parse(value!),
              ),
              // Add more fields for other inputs...
              SizedBox(height: 20),
              ElevatedButton(
                onPressed: _predict,
                child: Text('Predict'),
              ),
              SizedBox(height: 20),
              Text('Prediction: $_prediction'),
            ],
          ),
        ),
      ),
    );
  }
}
