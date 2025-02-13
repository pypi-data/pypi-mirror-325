import { i as pe, a as U, r as _e, g as he, w as T, d as ge, b as k, c as we } from "./Index-DcbX3t0J.js";
const v = window.ms_globals.React, F = window.ms_globals.React.useMemo, re = window.ms_globals.React.useState, oe = window.ms_globals.React.useEffect, fe = window.ms_globals.React.forwardRef, me = window.ms_globals.React.useRef, B = window.ms_globals.ReactDOM.createPortal, xe = window.ms_globals.internalContext.useContextPropsContext, L = window.ms_globals.internalContext.ContextPropsProvider, be = window.ms_globals.antd.Dropdown, Ie = window.ms_globals.createItemsContext.createItemsContext;
var ye = /\s/;
function ve(t) {
  for (var e = t.length; e-- && ye.test(t.charAt(e)); )
    ;
  return e;
}
var Ce = /^\s+/;
function Ee(t) {
  return t && t.slice(0, ve(t) + 1).replace(Ce, "");
}
var V = NaN, Re = /^[-+]0x[0-9a-f]+$/i, Se = /^0b[01]+$/i, ke = /^0o[0-7]+$/i, Oe = parseInt;
function q(t) {
  if (typeof t == "number")
    return t;
  if (pe(t))
    return V;
  if (U(t)) {
    var e = typeof t.valueOf == "function" ? t.valueOf() : t;
    t = U(e) ? e + "" : e;
  }
  if (typeof t != "string")
    return t === 0 ? t : +t;
  t = Ee(t);
  var o = Se.test(t);
  return o || ke.test(t) ? Oe(t.slice(2), o ? 2 : 8) : Re.test(t) ? V : +t;
}
var N = function() {
  return _e.Date.now();
}, Te = "Expected a function", Pe = Math.max, je = Math.min;
function Le(t, e, o) {
  var l, s, n, r, i, a, w = 0, g = !1, c = !1, _ = !0;
  if (typeof t != "function")
    throw new TypeError(Te);
  e = q(e) || 0, U(o) && (g = !!o.leading, c = "maxWait" in o, n = c ? Pe(q(o.maxWait) || 0, e) : n, _ = "trailing" in o ? !!o.trailing : _);
  function u(h) {
    var y = l, S = s;
    return l = s = void 0, w = h, r = t.apply(S, y), r;
  }
  function x(h) {
    return w = h, i = setTimeout(p, e), g ? u(h) : r;
  }
  function d(h) {
    var y = h - a, S = h - w, G = e - y;
    return c ? je(G, n - S) : G;
  }
  function m(h) {
    var y = h - a, S = h - w;
    return a === void 0 || y >= e || y < 0 || c && S >= n;
  }
  function p() {
    var h = N();
    if (m(h))
      return I(h);
    i = setTimeout(p, d(h));
  }
  function I(h) {
    return i = void 0, _ && l ? u(h) : (l = s = void 0, r);
  }
  function C() {
    i !== void 0 && clearTimeout(i), w = 0, l = a = s = i = void 0;
  }
  function f() {
    return i === void 0 ? r : I(N());
  }
  function E() {
    var h = N(), y = m(h);
    if (l = arguments, s = this, a = h, y) {
      if (i === void 0)
        return x(a);
      if (c)
        return clearTimeout(i), i = setTimeout(p, e), u(a);
    }
    return i === void 0 && (i = setTimeout(p, e)), r;
  }
  return E.cancel = C, E.flush = f, E;
}
var se = {
  exports: {}
}, A = {};
/**
 * @license React
 * react-jsx-runtime.production.min.js
 *
 * Copyright (c) Facebook, Inc. and its affiliates.
 *
 * This source code is licensed under the MIT license found in the
 * LICENSE file in the root directory of this source tree.
 */
var Fe = v, Ae = Symbol.for("react.element"), Ne = Symbol.for("react.fragment"), We = Object.prototype.hasOwnProperty, De = Fe.__SECRET_INTERNALS_DO_NOT_USE_OR_YOU_WILL_BE_FIRED.ReactCurrentOwner, Me = {
  key: !0,
  ref: !0,
  __self: !0,
  __source: !0
};
function le(t, e, o) {
  var l, s = {}, n = null, r = null;
  o !== void 0 && (n = "" + o), e.key !== void 0 && (n = "" + e.key), e.ref !== void 0 && (r = e.ref);
  for (l in e) We.call(e, l) && !Me.hasOwnProperty(l) && (s[l] = e[l]);
  if (t && t.defaultProps) for (l in e = t.defaultProps, e) s[l] === void 0 && (s[l] = e[l]);
  return {
    $$typeof: Ae,
    type: t,
    key: n,
    ref: r,
    props: s,
    _owner: De.current
  };
}
A.Fragment = Ne;
A.jsx = le;
A.jsxs = le;
se.exports = A;
var b = se.exports;
const {
  SvelteComponent: Be,
  assign: J,
  binding_callbacks: X,
  check_outros: Ue,
  children: ie,
  claim_element: ce,
  claim_space: He,
  component_subscribe: Y,
  compute_slots: ze,
  create_slot: Ge,
  detach: R,
  element: ae,
  empty: Q,
  exclude_internal_props: Z,
  get_all_dirty_from_scope: Ve,
  get_slot_changes: qe,
  group_outros: Je,
  init: Xe,
  insert_hydration: P,
  safe_not_equal: Ye,
  set_custom_element_data: ue,
  space: Qe,
  transition_in: j,
  transition_out: H,
  update_slot_base: Ze
} = window.__gradio__svelte__internal, {
  beforeUpdate: Ke,
  getContext: $e,
  onDestroy: et,
  setContext: tt
} = window.__gradio__svelte__internal;
function K(t) {
  let e, o;
  const l = (
    /*#slots*/
    t[7].default
  ), s = Ge(
    l,
    t,
    /*$$scope*/
    t[6],
    null
  );
  return {
    c() {
      e = ae("svelte-slot"), s && s.c(), this.h();
    },
    l(n) {
      e = ce(n, "SVELTE-SLOT", {
        class: !0
      });
      var r = ie(e);
      s && s.l(r), r.forEach(R), this.h();
    },
    h() {
      ue(e, "class", "svelte-1rt0kpf");
    },
    m(n, r) {
      P(n, e, r), s && s.m(e, null), t[9](e), o = !0;
    },
    p(n, r) {
      s && s.p && (!o || r & /*$$scope*/
      64) && Ze(
        s,
        l,
        n,
        /*$$scope*/
        n[6],
        o ? qe(
          l,
          /*$$scope*/
          n[6],
          r,
          null
        ) : Ve(
          /*$$scope*/
          n[6]
        ),
        null
      );
    },
    i(n) {
      o || (j(s, n), o = !0);
    },
    o(n) {
      H(s, n), o = !1;
    },
    d(n) {
      n && R(e), s && s.d(n), t[9](null);
    }
  };
}
function nt(t) {
  let e, o, l, s, n = (
    /*$$slots*/
    t[4].default && K(t)
  );
  return {
    c() {
      e = ae("react-portal-target"), o = Qe(), n && n.c(), l = Q(), this.h();
    },
    l(r) {
      e = ce(r, "REACT-PORTAL-TARGET", {
        class: !0
      }), ie(e).forEach(R), o = He(r), n && n.l(r), l = Q(), this.h();
    },
    h() {
      ue(e, "class", "svelte-1rt0kpf");
    },
    m(r, i) {
      P(r, e, i), t[8](e), P(r, o, i), n && n.m(r, i), P(r, l, i), s = !0;
    },
    p(r, [i]) {
      /*$$slots*/
      r[4].default ? n ? (n.p(r, i), i & /*$$slots*/
      16 && j(n, 1)) : (n = K(r), n.c(), j(n, 1), n.m(l.parentNode, l)) : n && (Je(), H(n, 1, 1, () => {
        n = null;
      }), Ue());
    },
    i(r) {
      s || (j(n), s = !0);
    },
    o(r) {
      H(n), s = !1;
    },
    d(r) {
      r && (R(e), R(o), R(l)), t[8](null), n && n.d(r);
    }
  };
}
function $(t) {
  const {
    svelteInit: e,
    ...o
  } = t;
  return o;
}
function rt(t, e, o) {
  let l, s, {
    $$slots: n = {},
    $$scope: r
  } = e;
  const i = ze(n);
  let {
    svelteInit: a
  } = e;
  const w = T($(e)), g = T();
  Y(t, g, (f) => o(0, l = f));
  const c = T();
  Y(t, c, (f) => o(1, s = f));
  const _ = [], u = $e("$$ms-gr-react-wrapper"), {
    slotKey: x,
    slotIndex: d,
    subSlotIndex: m
  } = he() || {}, p = a({
    parent: u,
    props: w,
    target: g,
    slot: c,
    slotKey: x,
    slotIndex: d,
    subSlotIndex: m,
    onDestroy(f) {
      _.push(f);
    }
  });
  tt("$$ms-gr-react-wrapper", p), Ke(() => {
    w.set($(e));
  }), et(() => {
    _.forEach((f) => f());
  });
  function I(f) {
    X[f ? "unshift" : "push"](() => {
      l = f, g.set(l);
    });
  }
  function C(f) {
    X[f ? "unshift" : "push"](() => {
      s = f, c.set(s);
    });
  }
  return t.$$set = (f) => {
    o(17, e = J(J({}, e), Z(f))), "svelteInit" in f && o(5, a = f.svelteInit), "$$scope" in f && o(6, r = f.$$scope);
  }, e = Z(e), [l, s, g, c, i, a, r, n, I, C];
}
class ot extends Be {
  constructor(e) {
    super(), Xe(this, e, rt, nt, Ye, {
      svelteInit: 5
    });
  }
}
const ee = window.ms_globals.rerender, W = window.ms_globals.tree;
function st(t, e = {}) {
  function o(l) {
    const s = T(), n = new ot({
      ...l,
      props: {
        svelteInit(r) {
          window.ms_globals.autokey += 1;
          const i = {
            key: window.ms_globals.autokey,
            svelteInstance: s,
            reactComponent: t,
            props: r.props,
            slot: r.slot,
            target: r.target,
            slotIndex: r.slotIndex,
            subSlotIndex: r.subSlotIndex,
            ignore: e.ignore,
            slotKey: r.slotKey,
            nodes: []
          }, a = r.parent ?? W;
          return a.nodes = [...a.nodes, i], ee({
            createPortal: B,
            node: W
          }), r.onDestroy(() => {
            a.nodes = a.nodes.filter((w) => w.svelteInstance !== s), ee({
              createPortal: B,
              node: W
            });
          }), i;
        },
        ...l.props
      }
    });
    return s.set(n), n;
  }
  return new Promise((l) => {
    window.ms_globals.initializePromise.then(() => {
      l(o);
    });
  });
}
function lt(t) {
  const [e, o] = re(() => k(t));
  return oe(() => {
    let l = !0;
    return t.subscribe((n) => {
      l && (l = !1, n === e) || o(n);
    });
  }, [t]), e;
}
function it(t) {
  const e = F(() => ge(t, (o) => o), [t]);
  return lt(e);
}
const ct = ["animationIterationCount", "borderImageOutset", "borderImageSlice", "borderImageWidth", "boxFlex", "boxFlexGroup", "boxOrdinalGroup", "columnCount", "columns", "flex", "flexGrow", "flexPositive", "flexShrink", "flexNegative", "flexOrder", "gridArea", "gridColumn", "gridColumnEnd", "gridColumnStart", "gridRow", "gridRowEnd", "gridRowStart", "lineClamp", "lineHeight", "opacity", "order", "orphans", "tabSize", "widows", "zIndex", "zoom", "fontWeight", "letterSpacing", "lineHeight"];
function at(t) {
  return t ? Object.keys(t).reduce((e, o) => {
    const l = t[o];
    return e[o] = ut(o, l), e;
  }, {}) : {};
}
function ut(t, e) {
  return typeof e == "number" && !ct.includes(t) ? e + "px" : e;
}
function z(t) {
  const e = [], o = t.cloneNode(!1);
  if (t._reactElement) {
    const s = v.Children.toArray(t._reactElement.props.children).map((n) => {
      if (v.isValidElement(n) && n.props.__slot__) {
        const {
          portals: r,
          clonedElement: i
        } = z(n.props.el);
        return v.cloneElement(n, {
          ...n.props,
          el: i,
          children: [...v.Children.toArray(n.props.children), ...r]
        });
      }
      return null;
    });
    return s.originalChildren = t._reactElement.props.children, e.push(B(v.cloneElement(t._reactElement, {
      ...t._reactElement.props,
      children: s
    }), o)), {
      clonedElement: o,
      portals: e
    };
  }
  Object.keys(t.getEventListeners()).forEach((s) => {
    t.getEventListeners(s).forEach(({
      listener: r,
      type: i,
      useCapture: a
    }) => {
      o.addEventListener(i, r, a);
    });
  });
  const l = Array.from(t.childNodes);
  for (let s = 0; s < l.length; s++) {
    const n = l[s];
    if (n.nodeType === 1) {
      const {
        clonedElement: r,
        portals: i
      } = z(n);
      e.push(...i), o.appendChild(r);
    } else n.nodeType === 3 && o.appendChild(n.cloneNode());
  }
  return {
    clonedElement: o,
    portals: e
  };
}
function dt(t, e) {
  t && (typeof t == "function" ? t(e) : t.current = e);
}
const O = fe(({
  slot: t,
  clone: e,
  className: o,
  style: l,
  observeAttributes: s
}, n) => {
  const r = me(), [i, a] = re([]), {
    forceClone: w
  } = xe(), g = w ? !0 : e;
  return oe(() => {
    var x;
    if (!r.current || !t)
      return;
    let c = t;
    function _() {
      let d = c;
      if (c.tagName.toLowerCase() === "svelte-slot" && c.children.length === 1 && c.children[0] && (d = c.children[0], d.tagName.toLowerCase() === "react-portal-target" && d.children[0] && (d = d.children[0])), dt(n, d), o && d.classList.add(...o.split(" ")), l) {
        const m = at(l);
        Object.keys(m).forEach((p) => {
          d.style[p] = m[p];
        });
      }
    }
    let u = null;
    if (g && window.MutationObserver) {
      let d = function() {
        var C, f, E;
        (C = r.current) != null && C.contains(c) && ((f = r.current) == null || f.removeChild(c));
        const {
          portals: p,
          clonedElement: I
        } = z(t);
        c = I, a(p), c.style.display = "contents", _(), (E = r.current) == null || E.appendChild(c);
      };
      d();
      const m = Le(() => {
        d(), u == null || u.disconnect(), u == null || u.observe(t, {
          childList: !0,
          subtree: !0,
          attributes: s
        });
      }, 50);
      u = new window.MutationObserver(m), u.observe(t, {
        attributes: !0,
        childList: !0,
        subtree: !0
      });
    } else
      c.style.display = "contents", _(), (x = r.current) == null || x.appendChild(c);
    return () => {
      var d, m;
      c.style.display = "", (d = r.current) != null && d.contains(c) && ((m = r.current) == null || m.removeChild(c)), u == null || u.disconnect();
    };
  }, [t, g, o, l, n, s]), v.createElement("react-child", {
    ref: r,
    style: {
      display: "contents"
    }
  }, ...i);
});
function ft(t) {
  return /^(?:async\s+)?(?:function\s*(?:\w*\s*)?\(|\([\w\s,=]*\)\s*=>|\(\{[\w\s,=]*\}\)\s*=>|function\s*\*\s*\w*\s*\()/i.test(t.trim());
}
function mt(t, e = !1) {
  try {
    if (we(t))
      return t;
    if (e && !ft(t))
      return;
    if (typeof t == "string") {
      let o = t.trim();
      return o.startsWith(";") && (o = o.slice(1)), o.endsWith(";") && (o = o.slice(0, -1)), new Function(`return (...args) => (${o})(...args)`)();
    }
    return;
  } catch {
    return;
  }
}
function D(t, e) {
  return F(() => mt(t, e), [t, e]);
}
function te(t, e) {
  const o = F(() => v.Children.toArray(t.originalChildren || t).filter((n) => n.props.node && !n.props.node.ignore && (!e && !n.props.nodeSlotKey || e && e === n.props.nodeSlotKey)).sort((n, r) => {
    if (n.props.node.slotIndex && r.props.node.slotIndex) {
      const i = k(n.props.node.slotIndex) || 0, a = k(r.props.node.slotIndex) || 0;
      return i - a === 0 && n.props.node.subSlotIndex && r.props.node.subSlotIndex ? (k(n.props.node.subSlotIndex) || 0) - (k(r.props.node.subSlotIndex) || 0) : i - a;
    }
    return 0;
  }).map((n) => n.props.node.target), [t, e]);
  return it(o);
}
function de(t, e, o) {
  const l = t.filter(Boolean);
  if (l.length !== 0)
    return l.map((s, n) => {
      var w;
      if (typeof s != "object")
        return e != null && e.fallback ? e.fallback(s) : s;
      const r = {
        ...s.props,
        key: ((w = s.props) == null ? void 0 : w.key) ?? (o ? `${o}-${n}` : `${n}`)
      };
      let i = r;
      Object.keys(s.slots).forEach((g) => {
        if (!s.slots[g] || !(s.slots[g] instanceof Element) && !s.slots[g].el)
          return;
        const c = g.split(".");
        c.forEach((p, I) => {
          i[p] || (i[p] = {}), I !== c.length - 1 && (i = r[p]);
        });
        const _ = s.slots[g];
        let u, x, d = (e == null ? void 0 : e.clone) ?? !1, m = e == null ? void 0 : e.forceClone;
        _ instanceof Element ? u = _ : (u = _.el, x = _.callback, d = _.clone ?? d, m = _.forceClone ?? m), m = m ?? !!x, i[c[c.length - 1]] = u ? x ? (...p) => (x(c[c.length - 1], p), /* @__PURE__ */ b.jsx(L, {
          params: p,
          forceClone: m,
          children: /* @__PURE__ */ b.jsx(O, {
            slot: u,
            clone: d
          })
        })) : /* @__PURE__ */ b.jsx(L, {
          forceClone: m,
          children: /* @__PURE__ */ b.jsx(O, {
            slot: u,
            clone: d
          })
        }) : i[c[c.length - 1]], i = r;
      });
      const a = (e == null ? void 0 : e.children) || "children";
      return s[a] ? r[a] = de(s[a], e, `${n}`) : e != null && e.children && (r[a] = void 0, Reflect.deleteProperty(r, a)), r;
    });
}
function ne(t, e) {
  return t ? /* @__PURE__ */ b.jsx(O, {
    slot: t,
    clone: e == null ? void 0 : e.clone
  }) : null;
}
function M({
  key: t,
  slots: e,
  targets: o
}, l) {
  return e[t] ? (...s) => o ? o.map((n, r) => /* @__PURE__ */ b.jsx(L, {
    params: s,
    forceClone: (l == null ? void 0 : l.forceClone) ?? !0,
    children: ne(n, {
      clone: !0,
      ...l
    })
  }, r)) : /* @__PURE__ */ b.jsx(L, {
    params: s,
    forceClone: (l == null ? void 0 : l.forceClone) ?? !0,
    children: ne(e[t], {
      clone: !0,
      ...l
    })
  }) : void 0;
}
const {
  useItems: pt,
  withItemsContextProvider: _t,
  ItemHandler: gt
} = Ie("antd-menu-items"), wt = st(_t(["menu.items"], ({
  getPopupContainer: t,
  slots: e,
  children: o,
  dropdownRender: l,
  buttonsRender: s,
  setSlotParams: n,
  value: r,
  ...i
}) => {
  var x, d, m;
  const a = D(t), w = D(l), g = D(s), c = te(o, "buttonsRender"), _ = te(o), {
    items: {
      "menu.items": u
    }
  } = pt();
  return /* @__PURE__ */ b.jsxs(b.Fragment, {
    children: [/* @__PURE__ */ b.jsx("div", {
      style: {
        display: "none"
      },
      children: _.length > 0 ? null : o
    }), /* @__PURE__ */ b.jsx(be.Button, {
      ...i,
      buttonsRender: c.length ? M({
        key: "buttonsRender",
        slots: e,
        setSlotParams: n,
        targets: c
      }) : g,
      menu: {
        ...i.menu,
        items: F(() => {
          var p;
          return ((p = i.menu) == null ? void 0 : p.items) || de(u, {
            clone: !0
          }) || [];
        }, [u, (x = i.menu) == null ? void 0 : x.items]),
        expandIcon: e["menu.expandIcon"] ? M({
          slots: e,
          setSlotParams: n,
          key: "menu.expandIcon"
        }, {
          clone: !0
        }) : (d = i.menu) == null ? void 0 : d.expandIcon,
        overflowedIndicator: e["menu.overflowedIndicator"] ? /* @__PURE__ */ b.jsx(O, {
          slot: e["menu.overflowedIndicator"]
        }) : (m = i.menu) == null ? void 0 : m.overflowedIndicator
      },
      getPopupContainer: a,
      dropdownRender: e.dropdownRender ? M({
        slots: e,
        setSlotParams: n,
        key: "dropdownRender"
      }) : w,
      icon: e.icon ? /* @__PURE__ */ b.jsx(O, {
        slot: e.icon
      }) : i.icon,
      children: _.length > 0 ? o : r
    })]
  });
}));
export {
  wt as DropdownButton,
  wt as default
};
