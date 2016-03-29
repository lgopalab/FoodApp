<%@page import="java.sql.*"%>
<%@ page import="java.sql.DriverManager" %>
<%@page import="java.sql.Connection.*"%>
<html>
<body>

<br><br>
<form method="post" name="form">
<table border="1">
<tr><th>Sno</th><th>Name</th></tr>
<%
Connection con = null;
String url = "jdbc:mysql://localhost:3306/";
String db = "TEST";
String driver = "com.mysql.jdbc.Driver";
String userName ="root";
String password="123";

int sumcount=0;
Statement st;
Class.forName(driver).newInstance();
con = (Connection) DriverManager.getConnection(url+db,userName,password);
//java.sql.Connection con = DriverManager.getConnection("jdbc:mysql://localhost:3306/test","root","123"); 
String query = "select * from TEST";
st = con.createStatement();
ResultSet rs = st.executeQuery(query);
%>
<%
while(rs.next()){
%>
<tr><td><%=rs.getString(1)%></td>
<td><%=rs.getString(2)%></td>
</tr>
<%
}
%>
</table>
</form>
</body>
</html>