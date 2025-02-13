import unittest
from app import predict

# sms-spam-detection/test_app.py


class TestSpamDetection(unittest.TestCase):
    def test_predict_spam(self):
        message = "Congratulations! You've won a $1000 Walmart gift card. Go to http://bit.ly/123456 to claim now."
        prediction, confidence = predict(message)
        self.assertEqual(prediction, 'scam')  
        self.assertGreater(confidence, 0.5)

    def test_predict_ham(self):
        message = "Hey, are we still meeting for lunch tomorrow?"
        prediction, confidence = predict(message)
        self.assertEqual(prediction, 'trust')  
        self.assertGreater(confidence, 0.5)

if __name__ == '__main__':
    unittest.main()