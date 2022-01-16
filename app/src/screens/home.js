import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image, Button, ImageBackground, Linking } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import Svg, { Line, Circle } from 'react-native-svg';
import { Icon, Input } from 'react-native-elements'
import { useFonts } from 'expo-font';
import { ScrollView, TextInput, TouchableOpacity } from 'react-native-gesture-handler';





export default function Home() {
    const navigation = useNavigation();
    var i =0;
    const [estimate, setEstimate] = useState('');
    const [bill, setBill] = useState('10');
    var datesArr = []
    for(i=1;i<31;i++){
        datesArr.push({"day":i.toString(), "month":"JAN","available":i>16?true:false})
    }
    const [dates, setDates] = useState({
        dates:datesArr
    })
    const [doc, setDoc] = useState({"name":"Dr. Tri T. Nguyen, M.D.", "description":"I started having severe knee pain over 18 months ago. I was not seen in person just got a telephone diagnosis. the pain is inside my knee no swelling it's severe when it starts. I eventually got an MRI a couple of month ago. the MRI shows basic wear no arthritis. it seems to flare up and its debilitating."})

    const [languages, setLanguages] = useState({
        languages:["English", "French", "Spanish"]
    })
    var timeArr = []
    for(i=0;i<24;i++){
        timeArr.push({"time":i+":"+(i%2?"00":"30"),"available":i>9?true:false})
    }
    const [timeslots, setTimeslots] = useState({
        timeslots:timeArr
    })
    console.log(timeslots)
    const _updateDate = (i,available) => {
        datesArr[i-1] = {"day":i.toString(), "month":"JAN","available":!available?true:false};
        console.log(datesArr[i]);
        setDates({dates:datesArr});
    }
    const _updateTime = (i,available) => {
        timeArr[i] = {"time":i+":"+(i%2?"00":"30"),"available":!available?true:false};
        console.log(timeArr[i]);
        setTimeslots({timeslots:timeArr});
    }

    const _viewLanguages = languages.languages.map((item => {
        return(
        <View style={{borderRadius:10, borderColor:"#000", borderWidth:1, width:70, paddingVertical:5, marginVertical:5, marginHorizontal:5}}>
            <Text style={{fontWeight:'bold', fontSize:12, textAlign:'center', color:"#000"}}>{item}</Text>
            </View>
        )
    }))

    const _viewDates = dates.dates.map((item)=>{
        return(
        <TouchableOpacity onPress={()=>_updateDate(parseInt(item.day),item.available)} disabled={item.available?false:true}>
        <View style={{borderRadius:10, borderColor:!item.available?"#EAEAEA":"#000", borderWidth:1, width:70, paddingVertical:10, marginVertical:30, marginHorizontal:10}}>
        <Text style={{fontWeight:'bold', fontSize:30, textAlign:'center', color:!item.available?"#EAEAEA":"#000"}}>{item.day}</Text>
        <Text style={{fontWeight:'bold', fontSize:14, textAlign:'center', color:!item.available?"#EAEAEA":"#000"}}>{item.month}</Text>
        </View></TouchableOpacity>
        )});

    const _viewTime = timeslots.timeslots.map((item, index)=>{
        return(
        <TouchableOpacity disabled={item.available?false:true} onPress={()=>_updateTime(index, item.available)}>
        <View style={{borderRadius:10, borderColor:!item.available?"#EAEAEA":"#000", borderWidth:1, width:70, paddingVertical:10, marginVertical:5, marginHorizontal:10}}>
        <Text style={{fontWeight:'bold', fontSize:14, textAlign:'center', color:!item.available?"#EAEAEA":"#000"}}>{item.time}</Text>
        </View></TouchableOpacity>
        )});
    
  
    
   
    return(
        <View style={styles.container}>
            <View style={{flexDirection:'row'}}>
                <Icon name="arrowleft" type="antdesign"></Icon>
                <Text style={{marginLeft:'5%', fontWeight:'bold', fontSize:16}}>Home</Text>
            </View>
            <Text style={{marginTop:'0.5%', fontWeight:'bold', fontSize:23}}>Hello, Angela!</Text>
            <Text style={{marginTop:'5%', fontWeight:'bold', fontSize:13}}>Upcoming Appointment</Text>
        
        <View style={{marginTop:'5%'}}>
            <Image source={require('../assets/doc.jpg')} style={{width:100, height:100, borderRadius:50, alignSelf:'center', marginVertical:'5%'}}></Image>
            <Text style={{fontWeight:'bold', textAlign:'center'}}>{doc.name} </Text>
            <View style={{flexDirection:'row', alignSelf:'center'}}>{_viewLanguages}</View>            
            <Text style={{fontWeight:'bold', textAlign:'left', marginHorizontal:'5%'}}>Your symptoms:</Text>
            <Text style={{textAlign:'justify', fontSize:12, marginHorizontal:'5%'}}>{doc.description} </Text>
        </View>
        {console.log(Date.now())}
        <TouchableOpacity disabled={Date.now()>1642331017546?false:true} onPress={()=>{setEstimate("200"); Linking.openURL("https://meet.jit.si/teamzeromeeting")}}><View style={{borderRadius:10, backgroundColor:Date.now()>1642331017546?"#000":"#EAEAEA", paddingVertical:'2.5%', marginTop:'5%'}}>
                <Text style={{color:"#FFF", fontWeight:'bold', textAlign:'center'}}>Start Meeting</Text></View></TouchableOpacity>
        <TouchableOpacity onPress={()=>{setEstimate("200")}}><View style={{borderRadius:10, backgroundColor:"#000", paddingVertical:'2.5%', marginTop:'1.5%'}}>
                <Text style={{color:"#FFF", fontWeight:'bold', textAlign:'center'}}>Chat</Text></View></TouchableOpacity>
                <TouchableOpacity><Text style={{color:"#000", fontWeight:'bold', textAlign:'center', fontSize:12, marginTop:'2.5%'}}>Cancel Appointment</Text></TouchableOpacity>


        <View style={{flexDirection:'row', justifyContent:'space-evenly', backgroundColor:"#000", borderRadius:20, padding:'3.5%', marginTop:'40%'}}>
        <Icon name="home" type="ionicon" color="#FFF"></Icon>
        <TouchableOpacity onPress={()=>navigation.navigate('Chat')}><Icon name="chatbubbles" type="ionicon" color="#666"></Icon></TouchableOpacity>
        <TouchableOpacity onPress={()=>navigation.navigate('Wallet')}><Icon name="wallet" type="font-awesome-5" color="#666"></Icon></TouchableOpacity>
    </View>
        </View>
    );}

const styles = StyleSheet.create({
    container: {
        height: '100%',
        position: 'relative',
        backgroundColor: '#FFF',
        paddingTop:'10%',
        paddingHorizontal:'5%'
    },
    header: {
        height: '55%',
        width: '100%',
        marginTop: '-5%',
        resizeMode: 'contain',
        alignSelf: 'center'
    },

});
