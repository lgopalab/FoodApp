<%@page import="java.sql.*"%>
<%@ page import="java.sql.DriverManager" %>
<%@page import="java.sql.Connection.*"%>
<html>
<body>

<br><br>
<table border="1">
<tr><th>Sno</th><th>Name</th></tr>
<%
Connection con = null;
String user ="root";
String pass="123";

int sumcount=0;
Statement st;
Class.forName("com.mysql.jdbc.Driver").newInstance();
con = (Connection) DriverManager.getConnection("jdbc:mysql://localhost:3306/TEST",user,pass);
String query = "select * from TEST";
st = con.createStatement();
ResultSet rs = st.executeQuery(query);

while(rs.next()){
%>
<tr>
<td><%=rs.getString(1)%></td>
<td><%=rs.getString(2)%></td>
</tr>
<%
}
%>
</table>
</body>
</html>