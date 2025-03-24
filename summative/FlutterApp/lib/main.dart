import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        primarySwatch: Colors.blue,
        fontFamily: 'Poppins',
      ),
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
  final Map<String, dynamic> _inputs = {};
  String _prediction = "";
  bool _isLoading = false;

  Future<void> _predict() async {
    if (_formKey.currentState!.validate()) {
      _formKey.currentState!.save();
      setState(() {
        _isLoading = true;
      });

      final url = Uri.parse('https://prediction-api-ife7.onrender.com/predict');
      try {
        final response = await http.post(
          url,
          headers: {'Content-Type': 'application/json'},
          body: json.encode(_inputs),
        );

        if (response.statusCode == 200) {
          final responseData = json.decode(response.body);
          final predictionValue = responseData['prediction'];
          final formattedPrediction = (predictionValue as double).toStringAsFixed(2);

          setState(() {
            _prediction = "Prediction: $formattedPrediction";
          });
        } else {
          setState(() {
            _prediction = "Error: ${response.statusCode} - ${response.body}";
          });
        }
      } catch (e) {
        setState(() {
          _prediction = "Error: Failed to connect to the API.";
        });
      } finally {
        setState(() {
          _isLoading = false;
        });
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Depression Prediction App", style: TextStyle(fontWeight: FontWeight.bold)),
        centerTitle: true,
        elevation: 0,
      ),
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            children: [
              _buildInputCard(),
              SizedBox(height: 20),
              _isLoading
                  ? CircularProgressIndicator()
                  : ElevatedButton(
                      onPressed: _predict,
                      style: ElevatedButton.styleFrom(
                        backgroundColor: Colors.teal,
                        padding: EdgeInsets.symmetric(horizontal: 40, vertical: 15),
                        shape: RoundedRectangleBorder(
                          borderRadius: BorderRadius.circular(10),
                        ),
                      ),
                      child: Text(
                        "Predict",
                        style: TextStyle(fontSize: 18, color: Colors.white),
                      ),
                    ),
              SizedBox(height: 20),
              if (_prediction.isNotEmpty)
                Container(
                  padding: EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: Colors.blue.shade50,
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Text(
                    _prediction,
                    style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.blue.shade900),
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildInputCard() {
    return Card(
      elevation: 5,
      shape: RoundedRectangleBorder(
        borderRadius: BorderRadius.circular(10),
      ),
      child: Padding(
        padding: EdgeInsets.all(16.0),
        child: Column(
          children: [
            _buildTextFormField("Gender (0 = Female, 1 = Male)", 'gender', isInt: true, icon: Icons.person),
            _buildTextFormField("Age", 'age', icon: Icons.cake),
            _buildTextFormField("Profession (Encoded Value)", 'profession', isInt: true, icon: Icons.work),
            _buildTextFormField("Academic Pressure", 'academic_pressure', icon: Icons.school),
            _buildTextFormField("Work Pressure", 'work_pressure', icon: Icons.work_outline),
            _buildTextFormField("CGPA", 'cgpa', icon: Icons.grade),
            _buildTextFormField("Study Satisfaction", 'study_satisfaction', icon: Icons.emoji_objects),
            _buildTextFormField("Job Satisfaction", 'job_satisfaction', icon: Icons.thumb_up),
            _buildTextFormField("Sleep Duration (Encoded Value)", 'sleep_duration', isInt: true, icon: Icons.bedtime),
            _buildTextFormField("Dietary Habits (Encoded Value)", 'dietary_habits', isInt: true, icon: Icons.fastfood),
            _buildTextFormField("Degree (Encoded Value)", 'degree', isInt: true, icon: Icons.school),
            _buildTextFormField("Suicidal Thoughts (0 = No, 1 = Yes)", 'suicidal_thoughts', isInt: true, icon: Icons.warning),
            _buildTextFormField("Work/Study Hours", 'work_study_hours', icon: Icons.access_time),
            _buildTextFormField("Financial Stress", 'financial_stress', icon: Icons.attach_money),
            _buildTextFormField("Family History (0 = No, 1 = Yes)", 'family_history', isInt: true, icon: Icons.family_restroom),
          ],
        ),
      ),
    );
  }

  Widget _buildTextFormField(String labelText, String key, {bool isInt = false, IconData? icon}) {
    return Padding(
      padding: EdgeInsets.only(bottom: 10),
      child: TextFormField(
        decoration: InputDecoration(
          labelText: labelText,
          prefixIcon: icon != null ? Icon(icon, color: Colors.teal) : null,
          border: OutlineInputBorder(
            borderRadius: BorderRadius.circular(10),
          ),
        ),
        keyboardType: TextInputType.number,
        validator: (value) {
          if (value == null || value.isEmpty) {
            return 'Please enter a value';
          }
          if (isInt && int.tryParse(value) == null) {
            return 'Please enter a valid integer';
          }
          if (!isInt && double.tryParse(value) == null) {
            return 'Please enter a valid number';
          }
          return null;
        },
        onSaved: (value) {
          if (isInt) {
            _inputs[key] = int.parse(value!);
          } else {
            _inputs[key] = double.parse(value!);
          }
        },
      ),
    );
  }
}
