import React, { useState, useCallback, useEffect } from 'react'
import { Text, View } from 'react-native';
import { GiftedChat } from 'react-native-gifted-chat'
import { Icon } from 'react-native-elements'
import { TouchableOpacity } from 'react-native-gesture-handler';

export default function Chat() {
  const [messages, setMessages] = useState([]);

  useEffect(() => {
    setMessages([
      {
        _id: 1,
        text: 'Hi Angela, let me know if you have any questions before the appointment.',
        createdAt: new Date(),
        user: {
          _id: 2,
          name: 'Meredith Grey',
          avatar: 'https://placeimg.com/140/140/any',
        },
      },
    ])
  }, [])

  const onSend = useCallback((messages = []) => {
    setMessages(previousMessages => GiftedChat.append(previousMessages, messages))
  }, [])

  return (
      <View style={{flex:1}}>
          <View style={{padding:'10%', backgroundColor:'#000', flexDirection:'row', borderBottomLeftRadius:10, borderBottomRightRadius:10}}>
              <Icon name="chevron-left" type="entypo" color="#FFF"></Icon>
              <Text style={{fontSize:20, fontWeight:'bold', color:"#FFF"}}>Doc</Text>
          </View>
    <GiftedChat
      messages={messages}
      onSend={messages => onSend(messages)}
      user={{
        _id: 1,
      }}
    />
    <View style={{flexDirection:'row', justifyContent:'space-evenly', backgroundColor:"#000", borderRadius:20, padding:'3.5%', marginTop:'5%', marginBottom:'2.5%'}}>
        <Icon name="home" type="ionicon" color="#666"></Icon>
        <Icon name="chatbubbles" type="ionicon" color="#FFF"></Icon>
        <TouchableOpacity onPress={()=>navigation.navigate('Wallet')}><Icon name="wallet" type="font-awesome-5" color="#666"></Icon></TouchableOpacity>
    </View>
    </View>
  )
}