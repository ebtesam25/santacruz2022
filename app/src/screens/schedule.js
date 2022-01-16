import React, { useState, useEffect } from 'react';
import { StyleSheet, Text, View, Image, Button, ImageBackground } from 'react-native';
import { useNavigation } from '@react-navigation/native';
import Svg, { Line, Circle } from 'react-native-svg';
import { Icon, Input } from 'react-native-elements'
import { useFonts } from 'expo-font';
import { ScrollView, TextInput, TouchableOpacity } from 'react-native-gesture-handler';





export default function Scheduler() {
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
    const [doc, setDoc] = useState({"name":"Dr. Tri T. Nguyen, M.D.", "description":"Dr. Tri T. Nguyen, M.D. hails from the Gulf Coast city of Lake Jackson, TX. He received his medical training at the University of Texas Southwestern in Dallas, and he completed his residency at the University of Texas Health Science Center in Houston."})

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
            {!estimate&&<>
            <View style={{flexDirection:'row'}}>
                <Icon name="arrowleft" type="antdesign"></Icon>
                <Text style={{marginLeft:'5%', fontWeight:'bold', fontSize:16}}>Appointment</Text>
            </View>
            <Text style={{marginTop:'5%', fontWeight:'bold', fontSize:13, marginBottom:'2.5%'}}>Describe your symptoms</Text>
            <TextInput placeholder="Explain your symptoms to get an estimate for appointment duration" style={{borderRadius:10, borderColor:"#EAEAEA", borderWidth:1, textAlign:'justify', textAlignVertical:'top', padding:'2.5%', fontSize:12}} multiline numberOfLines={4}></TextInput>
            <Text style={{marginTop:'5%', fontWeight:'bold', fontSize:13}}>Select Date</Text>
            <View style={{height:140}}>
            <ScrollView horizontal style={{height:100}}>
                {_viewDates}
            </ScrollView>
            </View>
            <Text style={{marginTop:'0.5%', fontWeight:'bold', fontSize:13}}>Select Time</Text>
            <View style={{flexDirection:'row', flexWrap:'wrap', marginTop:'5%'}}>
                {_viewTime}
            </View>
            <TouchableOpacity onPress={()=>{setEstimate("200")}}><View style={{borderRadius:10, backgroundColor:"#000", paddingVertical:'2.5%', marginTop:'5%'}}>
                <Text style={{color:"#FFF", fontWeight:'bold', textAlign:'center'}}>Get Estimate</Text></View></TouchableOpacity>
        </>}
        
        
        <View style={{marginTop:'15%'}}>
        <Text style={{fontWeight:'bold', fontSize:13, textAlign:'center'}}>In-network</Text>
            <Image source={require('../assets/doc.jpg')} style={{width:100, height:100, borderRadius:50, alignSelf:'center', marginVertical:'5%'}}></Image>
            <Text style={{fontWeight:'bold', textAlign:'center'}}>{doc.name} </Text>
            <View style={{flexDirection:'row', alignSelf:'center'}}>{_viewLanguages}</View>
            <Text style={{textAlign:'justify', fontSize:12, marginHorizontal:'5%'}}>{doc.description} </Text>
        </View>
        <View style={{marginTop:'15%'}}>
            <Text style={{fontWeight:'bold', fontSize:30,textAlign:'center'}}>{estimate}</Text>
            <Text style={{fontWeight:'bold', fontSize:13, textAlign:'center'}}>Estimated Duration</Text>
            <Text style={{fontWeight:'bold', fontSize:30, textAlign:'center'}}>{bill}</Text>
            <Text style={{fontWeight:'bold', fontSize:13, textAlign:'center'}}>Estimated Bill</Text>
        </View>
        <TouchableOpacity onPress={()=>{navigation.navigate('Home')}}><View style={{borderRadius:10, backgroundColor:"#000", paddingVertical:'2.5%', marginTop:'15%'}}>
                <Text style={{color:"#FFF", fontWeight:'bold', textAlign:'center'}}>Confirm Appointment</Text></View></TouchableOpacity>
                <TouchableOpacity><Text style={{color:"#000", fontWeight:'bold', textAlign:'center', fontSize:12, marginTop:'2.5%'}}>Cancel</Text></TouchableOpacity>
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
