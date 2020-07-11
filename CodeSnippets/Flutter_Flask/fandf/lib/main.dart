import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:convert';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: MyHomePage(),
    );
  }
}

class MyHomePage extends StatefulWidget {
  const MyHomePage({Key key}) : super(key: key);

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  var text = "hello";

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Center(
        child: Column(
          children: [
            SizedBox(height: 500),
            Text(text),
            FlatButton(
              onPressed: () async {
                final response = await http.get("http://127.0.0.1:5000/data");
                final decoded =
                    json.decode(response.body) as Map<String, dynamic>;

                setState(
                  () {
                    text = decoded["BAC"].toString();
                  },
                );
              },
              child: Text("Press"),
            ),
          ],
        ),
      ),
    );
  }
}
