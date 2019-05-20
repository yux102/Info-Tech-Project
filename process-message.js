const DialogFlow = require('dialogflow');

const projectId = 'newagent-c66fe';
const sessionId = '123456';
const languageCode = 'en';

const config = {
    credentials: {
        // private_key: process.env.DIALOGFLOW_PRIVATE_KEY,
        private_key: "-----BEGIN PRIVATE KEY-----\nMIIEvAIBADANBgkqhkiG9w0BAQEFAASCBKYwggSiAgEAAoIBAQCnbpvGU4KY/qr7\nbfIJoxzcfxSxkMjAYOW3J0Rw4w0jB4wBIi/Cm0PuDAIOmGuVkgIeYqtoXWBlxhuJ\nYWnoppkSQFTN7RJ94lsSa6dJowj+jsYJGo5wZ8KdaTP4PDpMsWmS1wr21/erRXB1\n0eniYz4B9TzSbkQdqJYMAguvvLjKcKqrX2a6LrgIYd9uSKCPp0BDQZxWXDMyQBuF\nSGCAcmECEWscPa2Fr0IhB1+TxGPf15B0rEJNAL3zUn+9KcItTf+2cn7JfZASWEic\nzZ9nUA8cZ/Jv1g3qg1IqEeNfv4WD2lyJbnqUr7k8MSO8JUEM6O6+t2640jn2TR3x\nnYWOp3GDAgMBAAECggEAIGFlUflDmBgkdCTCuvdnNQOEuoSANqhmtMGs3FIk78Hd\nYzi72NyTSh3bZfw3TkFjFIJLmQ75/iTOnYaP53UUxHFZlUvEmEDnEQxt2XFk42o0\nRX1zz6xZeHzolpj7Q2rKOqJJFg0VcnOm+LpEi8paqyFFBoNZvAynHCJnJTEP4eKR\nB5tc7B3rT4OohNkeK9ZqK9Iuql0lX08BaqjmzZuh9EUQzBPQS0CIPO4pWuvd4gYu\ngBEHmcPcFnmEEiMCnboKExprbFAYmqwNhYVo/gpFixndIub2Ny2EAL8yX/nUAyW8\n9KkefxeECOxRyCaN+hdews6IsMkR0ZaxJRrUjzEuAQKBgQDaANg3Ocqp4hqRTEQ5\nVOkxpuWWLCNF1q1/bTdutA35cGsB2H3rp/JcjBTAcLP3SIQbjwOrGTte8Y4Ick0j\n91K3aE1LI127010rjO3YkmVH7g2LZTQTqNTkIJmP/EPkJcnKmqpeT2SJ8/9Z+HtF\n/06f0Ye9Z4UZ0tjb9e9ouUJWAQKBgQDEnU+E6MmfX+84jRglfFqfOVTaoyGx1cNf\nk82TIUktJenPiNWNtqh/OqJeezv0dJWGHvrfwfneaMun00HqiNIXsiAumD91/IlL\nLsdL4I5R4jAvDqucEf/N11BzzY8Uz09frphrPaDXjZZ4oSDvNtHoCL2Vem3npDI5\nxEHZDGtvgwKBgANqjfjXlABzhZ0PR+ZqGTlo9yISUP8wLQnZKUw30Bw/kb22qcp+\nmEKxA0Y8veU7Iq7X3+PXgmGrgWFKgUD2CDrNjKCHzlk6J7SeAcAqEyI8bcPocxd3\nxtZIWH+0IVA6812UbOULc3Th+Pds+GmRZacFfo4OSDyuXC2ePgEzHgIBAoGAbcHH\nh1GQZFjgqTgSl7KAwEv384mHoMfNJgjThOPa/sogaMthM5gZHdU0mPvAb2m5osKe\nl9SoUSE9NzW2oV+5sKKuVnSFUK8mUYMOnGwB5vIWpd5RrHFb1KPy9IJ28k38aFSG\nH6+qn0oaCsMgKIn4ycg/VTegLOS7aQYHIExPmVMCgYAuhwjBZdQSvRur7hAedMR6\nh48gFFZdOHm4VZJujaDf112UDfcHErDLfMERawNL1k/tCD8na13ly/l060a6abJ6\ne4ceFtHAD8rHuVhW3Tizx/Z9FX4yRJQ1OXpr8qRJdINUaY5AGkH1MOASv/suBZiK\nDQe4R3mZThX23YUbo7dtng==\n-----END PRIVATE KEY-----\n",
        // client_email: process.env.DIALOGFLOW_CLIENT_EMAIL,
        client_email: "dialogflow-vwexjv@newagent-c66fe.iam.gserviceaccount.com",
    },
};

const sessionClient = new DialogFlow.SessionsClient(config);

const sessionPath = sessionClient.sessionPath(projectId, sessionId);

const processMessage = message => {
    const request = {
        session: sessionPath,
        queryInput: {
            text: {
                text: message,
                languageCode,
            },
        },
    };

    return new Promise(function (resolve, reject) {
        sessionClient
            .detectIntent(request)
            .then(responses => {
                console.log(responses);
                const result = responses[0].queryResult;
                console.log(result.fulfillmentText);
                resolve(result.fulfillmentText);
            })
            .catch(err => {
                console.error('ERROR:', err);
            });
    });
};

module.exports = processMessage;