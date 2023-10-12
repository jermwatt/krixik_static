def handler(event, context):
    
    body = '''
    <!DOCTYPE html>
    <html lang="english">
    <head>
        <title>exported project</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0" />
        <meta charset="utf-8" />
        <meta property="twitter:card" content="summary_large_image" />

        <style data-tag="reset-style-sheet">
        html {  line-height: 1.15;}body {  margin: 0;}* {  box-sizing: border-box;  border-width: 0;  border-style: solid;}p,li,ul,pre,div,h1,h2,h3,h4,h5,h6,figure,blockquote,figcaption {  margin: 0;  padding: 0;}button {  background-color: transparent;}button,input,optgroup,select,textarea {  font-family: inherit;  font-size: 100%;  line-height: 1.15;  margin: 0;}button,select {  text-transform: none;}button,[type="button"],[type="reset"],[type="submit"] {  -webkit-appearance: button;}button::-moz-focus-inner,[type="button"]::-moz-focus-inner,[type="reset"]::-moz-focus-inner,[type="submit"]::-moz-focus-inner {  border-style: none;  padding: 0;}button:-moz-focus,[type="button"]:-moz-focus,[type="reset"]:-moz-focus,[type="submit"]:-moz-focus {  outline: 1px dotted ButtonText;}a {  color: inherit;  text-decoration: inherit;}input {  padding: 2px 4px;}img {  display: block;}html { scroll-behavior: smooth  }
        </style>
        <style data-tag="default-style-sheet">
        html {
            font-family: Inter;
            font-size: 16px;
        }

        body {
            font-weight: 400;
            font-style:normal;
            text-decoration: none;
            text-transform: none;
            letter-spacing: normal;
            line-height: 1.15;
            color: var(--dl-color-gray-black);
            background-color: var(--dl-color-gray-white);

        }
        </style>
        <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&amp;display=swap"
        data-tag="font"
        />
        <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&amp;display=swap"
        data-tag="font"
        />
        <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Inter:wght@100;200;300;400;500;600;700;800;900&amp;display=swap"
        data-tag="font"
        />
        <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Cairo:wght@200;300;400;500;600;700;800;900&amp;display=swap"
        data-tag="font"
        />
        <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Cairo:wght@200;300;400;500;600;700;800;900&amp;display=swap"
        data-tag="font"
        />
        <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Cairo:wght@200;300;400;500;600;700;800;900&amp;display=swap"
        data-tag="font"
        />
        <link
        rel="stylesheet"
        href="https://fonts.googleapis.com/css2?family=Jura:wght@300;400;500;600;700&amp;display=swap"
        data-tag="font"
        />
    </head>
    <body>
        <link rel="stylesheet" href="./style.css" />
        <div>
        <link href="./index.css" rel="stylesheet" />

        <div class="homeframe-container">
            <div class="homeframe-homeframe">
            <div class="homeframe-group1">
                <img src="." alt="Background13" class="homeframe-background" />
                <span class="homeframe-text">
                <span>© Krixik 2023 - All rights reserved</span>
                </span>
                <span class="homeframe-text02">
                <span>
                    <span>The truly serverless</span>
                    <br />
                    <span>vector database alternative</span>
                </span>
                </span>
                <span class="homeframe-text07"><span>Coming soon</span></span>
                <span class="homeframe-text09">
                <span class="homeframe-text10">Kr</span>
                <span class="homeframe-text11">i</span>
                <span class="homeframe-text12">x</span>
                <span class="homeframe-text13">iK</span>
                </span>
            </div>
            </div>
        </div>
        </div>
    </body>
    </html>

    '''
    
    response = {
        'statusCode': 200,
        'headers': {"Content-Type": "text/html",},
        'body': body
    }
    
    return response