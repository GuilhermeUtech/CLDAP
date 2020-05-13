# Auto-generated by asn1ate v.0.6.0 from teste.asn
# (last modified on 2020-04-22 10:55:22.353923)

from pyasn1.type import univ, char, namedtype, namedval, tag, constraint, useful
from pyasn1.codec.ber.encoder import encode
from pyasn1.debug import hexdump
import threading
import time
from datetime import datetime
import socket

data_e_hora_atuais = datetime.now()

class ThreadOne(threading.Thread):
    def run(self):
        while(1):
            data_e_hora_atuais = datetime.now()
            if data_e_hora_atuais.month < 10:
                mes = '{:0>2}'.format(data_e_hora_atuais.month)
                
            else :
                mes = data_e_hora_atuais.month
            
            if data_e_hora_atuais.day < 10:
                dia = '{:0>2}'.format(data_e_hora_atuais.day)
                
            else:
                dia = data_e_hora_atuais.day
            
            if data_e_hora_atuais.hour < 10:
                hora = '{:0>2}'.format(data_e_hora_atuais.hour)

            else:
                hora = data_e_hora_atuais.hour

            if data_e_hora_atuais.minute < 10:
                minutos = '{:0>2}'.format(data_e_hora_atuais.minute)
            else:
                minutos = data_e_hora_atuais.minute

            if data_e_hora_atuais.second < 10:
                segundos = '{:0>2}'.format(data_e_hora_atuais.second)
            else:
                segundos = data_e_hora_atuais.second
            
            data_em_texto = '{}{}{}{}{}{}.0Z'.format(data_e_hora_atuais.year,mes,dia,hora, minutos, segundos)
            data_e_hora_atuais = data_em_texto
            return data_e_hora_atuais
            time.sleep(60)

maxInt = univ.Integer(2147483647)


class MessageID(univ.Integer):
    pass


MessageID.subtypeSpec = constraint.ValueRangeConstraint(0, maxInt)


class AbandonRequest(MessageID):
    pass


AbandonRequest.tagSet = MessageID.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatSimple, 16))


class LDAPString(univ.OctetString):
    pass


class AttributeDeion(LDAPString):
    pass


class AttributeValue(univ.OctetString):
    pass


class AttributeList(univ.SequenceOf):
    pass


AttributeList.componentType = univ.Sequence(componentType=namedtype.NamedTypes(
    namedtype.NamedType('type', AttributeDeion()),
    namedtype.NamedType('vals', univ.SetOf(componentType=AttributeValue()))
))


class LDAPDN(LDAPString):
    pass


class AddRequest(univ.Sequence):
    pass


AddRequest.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 8))
AddRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('entry', LDAPDN()),
    namedtype.NamedType('attributes', AttributeList())
)


class LDAPURL(LDAPString):
    pass


class Referral(univ.SequenceOf):
    pass


Referral.componentType = LDAPURL()


class LDAPResult(univ.Sequence):
    pass


LDAPResult.componentType = namedtype.NamedTypes(
    namedtype.NamedType('resultCode', univ.Enumerated(namedValues=namedval.NamedValues(('success', 0), ('operationsError', 1), ('protocolError', 2), ('timeLimitExceeded', 3), ('sizeLimitExceeded', 4), ('compareFalse', 5), ('compareTrue', 6), ('authMethodNotSupported', 7), ('strongAuthRequired', 8), ('referral', 10), ('adminLimitExceeded', 11), ('unavailableCriticalExtension', 12), ('confidentialityRequired', 13), ('saslBindInProgress', 14), ('noSuchAttribute', 16), ('undefinedAttributeType', 17), ('inappropriateMatching', 18), ('constraintViolation', 19), ('attributeOrValueExists', 20), ('invalidAttributeSyntax', 21), ('noSuchObject', 32), ('aliasProblem', 33), ('invalidDNSyntax', 34), ('aliasDereferencingProblem', 36), ('inappropriateAuthentication', 48), ('invalidCredentials', 49), ('insufficientAccessRights', 50), ('busy', 51), ('unavailable', 52), ('unwillingToPerform', 53), ('loopDetect', 54), ('namingViolation', 64), ('objectClassViolation', 65), ('notAllowedOnNonLeaf', 66), ('notAllowedOnRDN', 67), ('entryAlreadyExists', 68), ('objectClassModsProhibited', 69), ('affectsMultipleDSAs', 71), ('other', 80)))),
    namedtype.NamedType('matchedDN', LDAPDN()),
    namedtype.NamedType('errorMessage', LDAPString()),
    namedtype.OptionalNamedType('referral', Referral().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3)))
)


class AddResponse(LDAPResult):
    pass


AddResponse.tagSet = LDAPResult.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 9))


class AssertionValue(univ.OctetString):
    pass


class Attribute(univ.Sequence):
    pass


Attribute.componentType = namedtype.NamedTypes(
    namedtype.NamedType('type', AttributeDeion()),
    namedtype.NamedType('vals', univ.SetOf(componentType=AttributeValue()))
)


class AttributeDeionList(univ.SequenceOf):
    pass


AttributeDeionList.componentType = AttributeDeion()


class AttributeType(LDAPString):
    pass


class AttributeTypeAndValues(univ.Sequence):
    pass


AttributeTypeAndValues.componentType = namedtype.NamedTypes(
    namedtype.NamedType('type', AttributeDeion()),
    namedtype.NamedType('vals', univ.SetOf(componentType=AttributeValue()))
)


class AttributeValueAssertion(univ.Sequence):
    pass


AttributeValueAssertion.componentType = namedtype.NamedTypes(
    namedtype.NamedType('attributeDesc', AttributeDeion()),
    namedtype.NamedType('assertionValue', AssertionValue())
)


class SaslCredentials(univ.Sequence):
    pass


SaslCredentials.componentType = namedtype.NamedTypes(
    namedtype.NamedType('mechanism', LDAPString()),
    namedtype.OptionalNamedType('credentials', univ.OctetString())
)


class AuthenticationChoice(univ.Choice):
    pass


AuthenticationChoice.componentType = namedtype.NamedTypes(
    namedtype.NamedType('simple', univ.OctetString().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('sasl', SaslCredentials().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3)))
)


class BindRequest(univ.Sequence):
    pass


BindRequest.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 0))
BindRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('version', univ.Integer().subtype(subtypeSpec=constraint.ValueRangeConstraint(1, 127))),
    namedtype.NamedType('name', LDAPDN()),
    namedtype.NamedType('authentication', AuthenticationChoice())
)


class BindResponse(univ.Sequence):
    pass


BindResponse.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 1))
BindResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('resultCode', univ.Enumerated(namedValues=namedval.NamedValues(('success', 0), ('operationsError', 1), ('protocolError', 2), ('timeLimitExceeded', 3), ('sizeLimitExceeded', 4), ('compareFalse', 5), ('compareTrue', 6), ('authMethodNotSupported', 7), ('strongAuthRequired', 8), ('referral', 10), ('adminLimitExceeded', 11), ('unavailableCriticalExtension', 12), ('confidentialityRequired', 13), ('saslBindInProgress', 14), ('noSuchAttribute', 16), ('undefinedAttributeType', 17), ('inappropriateMatching', 18), ('constraintViolation', 19), ('attributeOrValueExists', 20), ('invalidAttributeSyntax', 21), ('noSuchObject', 32), ('aliasProblem', 33), ('invalidDNSyntax', 34), ('aliasDereferencingProblem', 36), ('inappropriateAuthentication', 48), ('invalidCredentials', 49), ('insufficientAccessRights', 50), ('busy', 51), ('unavailable', 52), ('unwillingToPerform', 53), ('loopDetect', 54), ('namingViolation', 64), ('objectClassViolation', 65), ('notAllowedOnNonLeaf', 66), ('notAllowedOnRDN', 67), ('entryAlreadyExists', 68), ('objectClassModsProhibited', 69), ('affectsMultipleDSAs', 71), ('other', 80)))),
    namedtype.NamedType('matchedDN', LDAPDN()),
    namedtype.NamedType('errorMessage', LDAPString()),
    namedtype.OptionalNamedType('referral', Referral().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
    namedtype.OptionalNamedType('serverSaslCreds', univ.OctetString().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7)))
)


class CompareRequest(univ.Sequence):
    pass


CompareRequest.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 14))
CompareRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('entry', LDAPDN()),
    namedtype.NamedType('ava', AttributeValueAssertion())
)


class CompareResponse(LDAPResult):
    pass


CompareResponse.tagSet = LDAPResult.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 15))


class LDAPOID(univ.OctetString):
    pass


class Control(univ.Sequence):
    pass


Control.componentType = namedtype.NamedTypes(
    namedtype.NamedType('controlType', LDAPOID()),
    namedtype.DefaultedNamedType('criticality', univ.Boolean().subtype(value=0)),
    namedtype.OptionalNamedType('controlValue', univ.OctetString())
)


class Controls(univ.SequenceOf):
    pass


Controls.componentType = Control()


class DelRequest(LDAPDN):
    pass


DelRequest.tagSet = LDAPDN.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatSimple, 10))


class DelResponse(LDAPResult):
    pass


DelResponse.tagSet = LDAPResult.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 11))


class ExtendedRequest(univ.Sequence):
    pass


ExtendedRequest.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 23))
ExtendedRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('requestName', LDAPOID().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.OptionalNamedType('requestValue', univ.OctetString().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1)))
)


class ExtendedResponse(univ.Sequence):
    pass


ExtendedResponse.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 24))
ExtendedResponse.componentType = namedtype.NamedTypes(
    namedtype.NamedType('resultCode', univ.Enumerated(namedValues=namedval.NamedValues(('success', 0), ('operationsError', 1), ('protocolError', 2), ('timeLimitExceeded', 3), ('sizeLimitExceeded', 4), ('compareFalse', 5), ('compareTrue', 6), ('authMethodNotSupported', 7), ('strongAuthRequired', 8), ('referral', 10), ('adminLimitExceeded', 11), ('unavailableCriticalExtension', 12), ('confidentialityRequired', 13), ('saslBindInProgress', 14), ('noSuchAttribute', 16), ('undefinedAttributeType', 17), ('inappropriateMatching', 18), ('constraintViolation', 19), ('attributeOrValueExists', 20), ('invalidAttributeSyntax', 21), ('noSuchObject', 32), ('aliasProblem', 33), ('invalidDNSyntax', 34), ('aliasDereferencingProblem', 36), ('inappropriateAuthentication', 48), ('invalidCredentials', 49), ('insufficientAccessRights', 50), ('busy', 51), ('unavailable', 52), ('unwillingToPerform', 53), ('loopDetect', 54), ('namingViolation', 64), ('objectClassViolation', 65), ('notAllowedOnNonLeaf', 66), ('notAllowedOnRDN', 67), ('entryAlreadyExists', 68), ('objectClassModsProhibited', 69), ('affectsMultipleDSAs', 71), ('other', 80)))),
    namedtype.NamedType('matchedDN', LDAPDN()),
    namedtype.NamedType('errorMessage', LDAPString()),
    namedtype.OptionalNamedType('referral', Referral().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
    namedtype.OptionalNamedType('responseName', LDAPOID().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 10))),
    namedtype.OptionalNamedType('response', univ.OctetString().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 11)))
)


class SubstringFilter(univ.Sequence):
    pass


SubstringFilter.componentType = namedtype.NamedTypes(
    namedtype.NamedType('type', AttributeDeion()),
    namedtype.NamedType('substrings', univ.SequenceOf(componentType=univ.Choice(componentType=namedtype.NamedTypes(
        namedtype.NamedType('initial', LDAPString().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
        namedtype.NamedType('any', LDAPString().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
        namedtype.NamedType('final', LDAPString().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2)))
    ))
    ))
)


class MatchingRuleId(LDAPString):
    pass


class MatchingRuleAssertion(univ.Sequence):
    pass


MatchingRuleAssertion.componentType = namedtype.NamedTypes(
    namedtype.OptionalNamedType('matchingRule', MatchingRuleId().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.OptionalNamedType('type', AttributeDeion().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 2))),
    namedtype.NamedType('matchValue', AssertionValue().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 3))),
    namedtype.DefaultedNamedType('dnAttributes', univ.Boolean().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 4)).subtype(value=0))
)


class Filter(univ.Choice):
    pass


Filter.componentType = namedtype.NamedTypes(
    namedtype.NamedType('and', univ.SetOf(componentType=Filter()).subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0))),
    namedtype.NamedType('or', univ.SetOf(componentType=Filter()).subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 1))),
    namedtype.NamedType('not', Filter().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 2))),
    namedtype.NamedType('equalityMatch', AttributeValueAssertion().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 3))),
    namedtype.NamedType('substrings', SubstringFilter().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 4))),
    namedtype.NamedType('greaterOrEqual', AttributeValueAssertion().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 5))),
    namedtype.NamedType('lessOrEqual', AttributeValueAssertion().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 6))),
    namedtype.NamedType('present', AttributeDeion().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 7))),
    namedtype.NamedType('approxMatch', AttributeValueAssertion().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 8))),
    namedtype.NamedType('extensibleMatch', MatchingRuleAssertion().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatConstructed, 9)))
)


class ModifyRequest(univ.Sequence):
    pass


ModifyRequest.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 6))
ModifyRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('object', LDAPDN()),
    namedtype.NamedType('modification', univ.SequenceOf(componentType=univ.Sequence(componentType=namedtype.NamedTypes(
        namedtype.NamedType('operation', univ.Enumerated(namedValues=namedval.NamedValues(('add', 0), ('delete', 1), ('replace', 2)))),
        namedtype.NamedType('modification', AttributeTypeAndValues())
    ))
    ))
)


class PartialAttributeList(univ.SequenceOf):
    pass


PartialAttributeList.componentType = univ.Sequence(componentType=namedtype.NamedTypes(
    namedtype.NamedType('type', AttributeDeion()),
    namedtype.NamedType('vals', univ.SetOf(componentType=AttributeValue()))
))


class SearchResultEntry(univ.Sequence):
    pass


SearchResultEntry.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 4))
SearchResultEntry.componentType = namedtype.NamedTypes(
    namedtype.NamedType('objectName', LDAPDN()),
    namedtype.NamedType('attributes', PartialAttributeList())
)


class SearchResultDone(LDAPResult):
    pass


SearchResultDone.tagSet = LDAPResult.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 5))


class ModifyDNResponse(LDAPResult):
    pass


ModifyDNResponse.tagSet = LDAPResult.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 13))


class RelativeLDAPDN(LDAPString):
    pass


class ModifyDNRequest(univ.Sequence):
    pass


ModifyDNRequest.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 12))
ModifyDNRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('entry', LDAPDN()),
    namedtype.NamedType('newrdn', RelativeLDAPDN()),
    namedtype.NamedType('deleteoldrdn', univ.Boolean()),
    namedtype.OptionalNamedType('newSuperior', LDAPDN().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))
)


class ModifyResponse(LDAPResult):
    pass


ModifyResponse.tagSet = LDAPResult.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 7))


class UnbindRequest(univ.Null):
    pass


UnbindRequest.tagSet = univ.Null.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatSimple, 2))


class SearchResultReference(univ.SequenceOf):
    pass


SearchResultReference.tagSet = univ.SequenceOf.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatSimple, 19))
SearchResultReference.componentType = LDAPURL()


class SearchRequest(univ.Sequence):
    pass


SearchRequest.tagSet = univ.Sequence.tagSet.tagExplicitly(tag.Tag(tag.tagClassApplication, tag.tagFormatConstructed, 3))
SearchRequest.componentType = namedtype.NamedTypes(
    namedtype.NamedType('baseObject', LDAPDN()),
    namedtype.NamedType('scope', univ.Enumerated(namedValues=namedval.NamedValues(('baseObject', 0), ('singleLevel', 1), ('wholeSubtree', 2)))),
    namedtype.NamedType('derefAliases', univ.Enumerated(namedValues=namedval.NamedValues(('neverDerefAliases', 0), ('derefInSearching', 1), ('derefFindingBaseObj', 2), ('derefAlways', 3)))),
    namedtype.NamedType('sizeLimit', univ.Integer().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, maxInt))),
    namedtype.NamedType('timeLimit', univ.Integer().subtype(subtypeSpec=constraint.ValueRangeConstraint(0, maxInt))),
    namedtype.NamedType('typesOnly', univ.Boolean()),
    namedtype.NamedType('filter', Filter()),
    namedtype.NamedType('attributes', AttributeDeionList())
)


class LDAPMessage(univ.Sequence):
    pass


LDAPMessage.componentType = namedtype.NamedTypes(
    namedtype.NamedType('messageID', MessageID()),
    namedtype.NamedType('protocolOp', univ.Choice(componentType=namedtype.NamedTypes(
        namedtype.NamedType('bindRequest', BindRequest()),
        namedtype.NamedType('bindResponse', BindResponse()),
        namedtype.NamedType('unbindRequest', UnbindRequest()),
        namedtype.NamedType('searchRequest', SearchRequest()),
        namedtype.NamedType('searchResEntry', SearchResultEntry()),
        namedtype.NamedType('searchResDone', SearchResultDone()),
        namedtype.NamedType('searchResRef', SearchResultReference()),
        namedtype.NamedType('modifyRequest', ModifyRequest()),
        namedtype.NamedType('modifyResponse', ModifyResponse()),
        namedtype.NamedType('addRequest', AddRequest()),
        namedtype.NamedType('addResponse', AddResponse()),
        namedtype.NamedType('delRequest', DelRequest()),
        namedtype.NamedType('delResponse', DelResponse()),
        namedtype.NamedType('modDNRequest', ModifyDNRequest()),
        namedtype.NamedType('modDNResponse', ModifyDNResponse()),
        namedtype.NamedType('compareRequest', CompareRequest()),
        namedtype.NamedType('compareResponse', CompareResponse()),
        namedtype.NamedType('abandonRequest', AbandonRequest()),
        namedtype.NamedType('extendedReq', ExtendedRequest()),
        namedtype.NamedType('extendedResp', ExtendedResponse())
    ))
    ),
    namedtype.OptionalNamedType('controls', Controls().subtype(explicitTag=tag.Tag(tag.tagClassContext, tag.tagFormatSimple, 0)))
)

objeto = LDAPMessage()
            
thingOne = ThreadOne()
x = thingOne.run()


#currentTime - gerando o BER para o currentTime
objeto['protocolOp']['searchResEntry']['attributes']['a']['type'] = 'currentTime'
objeto['protocolOp']['searchResEntry']['attributes']['a']['vals'].extend([x])

#messageId - gerando o BER para o messageId
objeto['messageID'] = 1

attributes = encode(objeto['protocolOp']['searchResEntry']['attributes']['a']['type'])
attributes1 = encode(objeto['protocolOp']['searchResEntry']['attributes']['a']['vals'])

attributes = attributes + attributes1

messageId = encode(objeto['messageID']).rstrip()

msg = '0\x84\x00\x00\x0bN'+messageId+'d\x84\x00\x00\x0bE\x04\x000\x84\x00\x00\x0b=0\x84\x00\x00\x00"'+attributes+"0\x84\x00\x00\x00Y\x04\x11subschemaSubentry1\x84\x00\x00\x00@\x04>CN=Aggregate,CN=Schema,CN=Configuration,DC=corp,DC=udesc,DC=br0\x84\x00\x00\x00w\x04\rdsServiceName1\x84\x00\x00\x00b\x04`CN=NTDS Settings,CN=DC-01-CCT,CN=Servers,CN=CCT,CN=Sites,CN=Configuration,DC=corp,DC=udesc,DC=br0\x84\x00\x00\x00\xde\x04\x0enamingContexts1\x84\x00\x00\x00\xc8\x04\x16DC=corp,DC=udesc,DC=br\x04'CN=Configuration,DC=corp,DC=udesc,DC=br\x041CN=Schema,CN=Configuration,DC=corp,DC=udesc,DC=br\x04(DC=DomainDnsZones,DC=corp,DC=udesc,DC=br\x04(DC=ForestDnsZones,DC=corp,DC=udesc,DC=br0\x84\x00\x00\x004\x04\x14defaultNamingContext1\x84\x00\x00\x00\x18\x04\x16DC=corp,DC=udesc,DC=br0\x84\x00\x00\x00N\x04\x13schemaNamingContext1\x84\x00\x00\x003\x041CN=Schema,CN=Configuration,DC=corp,DC=udesc,DC=br0\x84\x00\x00\x00K\x04\x1aconfigurationNamingContext1\x84\x00\x00\x00)\x04'CN=Configuration,DC=corp,DC=udesc,DC=br0\x84\x00\x00\x007\x04\x17rootDomainNamingContext1\x84\x00\x00\x00\x18\x04\x16DC=corp,DC=udesc,DC=br0\x84\x00\x00\x03\xa9\x04\x10supportedControl1\x84\x00\x00\x03\x91\x04\x161.2.840.113556.1.4.319\x04\x161.2.840.113556.1.4.801\x04\x161.2.840.113556.1.4.473\x04\x161.2.840.113556.1.4.528\x04\x161.2.840.113556.1.4.417\x04\x161.2.840.113556.1.4.619\x04\x161.2.840.113556.1.4.841\x04\x161.2.840.113556.1.4.529\x04\x161.2.840.113556.1.4.805\x04\x161.2.840.113556.1.4.521\x04\x161.2.840.113556.1.4.970\x04\x171.2.840.113556.1.4.1338\x04\x161.2.840.113556.1.4.474\x04\x171.2.840.113556.1.4.1339\x04\x171.2.840.113556.1.4.1340\x04\x171.2.840.113556.1.4.1413\x04\x172.16.840.1.113730.3.4.9\x04\x182.16.840.1.113730.3.4.10\x04\x171.2.840.113556.1.4.1504\x04\x171.2.840.113556.1.4.1852\x04\x161.2.840.113556.1.4.802\x04\x171.2.840.113556.1.4.1907\x04\x171.2.840.113556.1.4.1948\x04\x171.2.840.113556.1.4.1974\x04\x171.2.840.113556.1.4.1341\x04\x171.2.840.113556"

PORT = 389
HOST = '10.60.1.19' #host qualquer
udp = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
dest = (HOST, PORT)

udp.sendto(msg, dest)
udp.close()