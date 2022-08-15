        public XmlDocument AplicaAssinatura(XmlDocument docXML, string uri, X509Certificate2 cert)
        {
            try
            {
                X509Certificate2 X509Cert = cert;

                // Cria o objeto XML assinado
                SignedXml signedXml = new SignedXml(docXML);
                // Assina com a chave privada
                signedXml.SigningKey = X509Cert.PrivateKey;
                // Atribui o método de canonização
                signedXml.SignedInfo.CanonicalizationMethod = "http://www.w3.org/TR/2001/REC-xml-c14n-20010315";
                // Atribui o método para assinatura
                signedXml.SignedInfo.SignatureMethod = "http://www.w3.org/2000/09/xmldsig#rsa-sha1";
                // Cria a referencia
                Reference reference = new Reference("");
                // Pega a URI para ser assinada
                XmlAttributeCollection _Uri = docXML.GetElementsByTagName(uri).Item(0).Attributes;
                foreach (XmlAttribute _atributo in _Uri)
                {
                    if (_atributo.Name == "Id")
                        reference.Uri = "#" + _atributo.InnerText;
                }
                // Adiciona o envelope à referência
                XmlDsigEnvelopedSignatureTransform env = new XmlDsigEnvelopedSignatureTransform();
                reference.AddTransform(env);

                XmlDsigC14NTransform c14 = new XmlDsigC14NTransform();
                reference.AddTransform(c14);

                // Atribui o método do Hash
                reference.DigestMethod = "http://www.w3.org/2000/09/xmldsig#sha1";
                // Adiciona a referencia ao XML assinado
                signedXml.AddReference(reference);
                // Cria o objeto keyInfo
                KeyInfo keyInfo = new KeyInfo();
                // Carrega a informação da KeyInfo
                KeyInfoClause rsaKeyVal = new RSAKeyValue((RSA)X509Cert.PrivateKey);
                KeyInfoX509Data x509Data = new KeyInfoX509Data(X509Cert);
                //x509Data.AddSubjectName(X509Cert.SubjectName.Name.ToString());
                keyInfo.AddClause(x509Data);
                //keyInfo.AddClause(rsaKeyVal);
                // Adiciona a KeyInfo
                signedXml.KeyInfo = keyInfo;
                // Atribui uma ID à assinatura
                //signedXml.Signature.Id = "#" + uri;
                // Efetiva a assinatura
                signedXml.ComputeSignature();
                bool signed = signedXml.CheckSignature(cert, true);
                // Obtem o XML assinado
                XmlElement xmlDigitalSignature = signedXml.GetXml();
                // Adiciona o elemento assinado ao XML
                docXML.DocumentElement.AppendChild(docXML.ImportNode(xmlDigitalSignature, true));

                // Retorna o XML
                return docXML;
            }
            catch (Exception erro) { throw erro; }
		}